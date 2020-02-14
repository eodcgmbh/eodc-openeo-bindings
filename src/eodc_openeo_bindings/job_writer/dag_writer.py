import os
from shutil import copyfile
from typing import Tuple, List

from eodc_openeo_bindings.job_writer.file_handler import BasicFileHandler
from eodc_openeo_bindings.job_writer.job_writer import JobWriter
from eodc_openeo_bindings.openeo_to_eodatareaders import openeo_to_eodatareaders


class AirflowDagWriter(JobWriter):

    def __init__(self, job_id, user_name, process_graph_json, job_data, user_email=None, job_description=None,
                 parallelize_tasks=False, vrt_only=False):
        self.job_id = job_id
        self.user_name = user_name
        self.user_email = user_email
        self.job_description = job_description if job_description else 'No description provided'
        self.parallelize_task = parallelize_tasks
        self.vrt_only = vrt_only
        self.nodes = None
        self.graph = None
        super().__init__(process_graph_json, job_data, BasicFileHandler, self.get_dag_filepath())

        self.not_parallelizable_func = (
            'filter_bands',
            'filter_bbox',
            'filter_temporal',
            'eo_array_element'
        )

    def get_dag_filepath(self):
        dag_name = f'dag_{self.job_id}'
        if self.parallelize_task:
            dag_name += '_parallelize'
        return dag_name + '.py'

    def get_default_filepath(self) -> str:
        return 'test_dag.py'

    def write_and_move_job(self):
        super().write_job()
        self.move_dag()

    def move_dag(self):
        # Move file to DAGs folder (must copy/delete because of different volume mounts)
        copyfile(self.file_handler.filepath, os.environ.get('AIRFLOW_DAGS') + "/" + self.file_handler.filepath)
        os.remove(self.file_handler.filepath)

    def get_imports(self) -> str:
        return '''\
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import eoDataReadersOp
'''

    def get_additional_header(self):
        # dag default args and dag instance
        return f'''\
default_args = {{
    'owner': "{self.user_name}",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "{self.user_email}",
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': None,
}}

dag = DAG(dag_id="{self.job_id}",
          description="{self.job_description}",
          catchup=True,
          default_args=default_args)
'''

    def get_task_txt(self, task_id, filepaths, process_graph, quotes):
        return f'''\
{task_id} = eoDataReadersOp(task_id='{task_id}',
                        dag=dag,
                        input_filepaths={quotes}{filepaths}{quotes},
                        input_params={process_graph}
                        )

'''

    def get_dependencies_txt(self, node_id, dependencies):
        return f'''\
{node_id}.set_upstream([{",".join(map(str, dependencies))}])

'''

    def _get_node_info(self, node):
        node_id = node[0]
        params = node[1]
        filepaths = node[2]
        node_dependencies = node[3]

        params, node_id = self._check_node_id_with_original_dag(params, node_id)
        if node_dependencies:
            node_dependencies = self.utils.get_existing_node(self.job_data, node_dependencies)

        return node_id, params, filepaths, node_dependencies

    def _check_key_is_parallelizable(self, params: List[dict], key: str):
        key_exists, _, _ = self.utils.check_params_key(params, key)

        parallelizable = False
        for item in params:
            # TODO could there be multiple function?
            if 'f_input' in item.keys():
                if item['f_input']['f_name'] not in self.not_parallelizable_func:
                    parallelizable = True

        return parallelizable

    def _check_node_id_with_original_dag(self, params, node_id):
        # Retrieve node_ids of original DAG ( useful only if re-running to parallelize, else it does nothing)
        node_id_orig = self.utils.get_existing_node(self.job_data, node_id)[0]
        if node_id != node_id_orig:
            params[0]['folder_name'] = params[0]['folder_name'].replace(node_id, node_id_orig)
        return params, node_id_orig

    def expand_node_dependencies(self, node_dependencies, dep_subnodes, split_dependencies=False):
        """
        Expand dependencies, in case a node had been split because of parallelization.
        """

        node_dependencies2 = []
        max_n = 1
        for dep in node_dependencies:
            if dep in dep_subnodes.keys():
                if split_dependencies:
                    node_dependencies2.append(dep_subnodes[dep])
                    max_n = max(max_n, len(dep_subnodes[dep]))
                else:
                    node_dependencies2.extend(dep_subnodes[dep])
            else:
                if split_dependencies:
                    node_dependencies2.append([dep])
                else:
                    node_dependencies2.append(dep)

        if split_dependencies:
            for k, dep in enumerate(node_dependencies2):
                if max_n > len(dep) > 1:
                    print('somethign wrokńg here.')
                if len(dep) < max_n:
                    node_dependencies2[k] = node_dependencies2[k] * max_n

            node_dependencies3 = []
            for k in range(max_n):
                tmp_deps = []
                for item in node_dependencies2:
                    tmp_deps.append(item[k])
                node_dependencies3.append(tmp_deps)

        else:
            node_dependencies3 = [node_dependencies2]

        return node_dependencies3

    def get_nodes(self) -> Tuple[dict, list]:
        if not self.nodes:
            self.nodes, self.graph = openeo_to_eodatareaders(self.process_graph_json, self.job_data, vrt_only=self.vrt_only)

        # Add nodes
        parallel_nodes\
            = {}
        dep_subnodes = {}
        translated_nodes = {}
        for node in self.nodes:
            node_id, params, filepaths, node_dependencies = self._get_node_info(node)

            # Check node can be parallelized if requested
            parallel_node = False
            if self.parallelize_task:
                parallel_node = True
                if not self._check_key_is_parallelizable(params, 'per_file'):
                    parallel_node = False
                if not node_dependencies or filepaths:
                    parallel_node = False

            if node_dependencies:
                filepaths = self.utils.get_filepaths_from_dependencies(node_dependencies, self.job_data,
                                                                       parallelize=parallel_node)
            if not filepaths or len(filepaths) <= 1:
                parallel_node = False

            if parallel_node:
                dep_subnodes[node_id] = []
                N_deps = len(filepaths)
                N_files = len(filepaths[0])
                for counter_1 in range(N_files):
                    in_files = []
                    for counter_2 in range(N_deps):
                        in_files.append(filepaths[counter_2][counter_1])
                    node_sub_id = node_id + '_' + str(counter_1 + 1)
                    quotes = "" if isinstance(in_files, list) else "'"
                    translated_nodes[node_sub_id] = self.get_task_txt(task_id=node_sub_id, filepaths=in_files, process_graph=params, quotes=quotes)
                    dep_subnodes[node_id].append(node_sub_id)
            else:
                translated_nodes[node_id] = self.get_task_txt(task_id=node_id, filepaths=filepaths,
                                                              process_graph=params, quotes="")
            parallel_nodes[node_id] = parallel_node

        # Add node dependencies
        for node in self.nodes:
            node_id, params, _, node_dependencies = self._get_node_info(node)

            if node_dependencies:
                node_dependencies2 = self.expand_node_dependencies(node_dependencies, dep_subnodes, parallel_nodes[node_id])
                if parallel_nodes[node_id]:
                    for k, sub_node_id in enumerate(dep_subnodes[node_id]):
                        index = k if len(node_dependencies2) > k else 0
                        translated_nodes[f'dep_{sub_node_id}'] = self.get_dependencies_txt(sub_node_id, node_dependencies2[index])
                else:
                    for dep_list in node_dependencies2:
                        translated_nodes[f'dep_{node_id}'] = self.get_dependencies_txt(node_id, dep_list)

        # 2nd output needed for compatibility with main JobWriter
        return translated_nodes, list(translated_nodes.keys())
