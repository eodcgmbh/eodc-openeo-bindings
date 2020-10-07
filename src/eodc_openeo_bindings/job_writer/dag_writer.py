import os
from copy import deepcopy
import json
from shutil import copyfile
from typing import Tuple, List, Optional, Union, Dict

from eodc_openeo_bindings.job_writer.job_domain import AirflowDagDomain
from eodc_openeo_bindings.job_writer.job_writer import JobWriter
from eodc_openeo_bindings.job_writer.utils import JobIdExtension
from eodc_openeo_bindings.openeo_to_eodatareaders import openeo_to_eodatareaders


class AirflowDagWriter(JobWriter):

    def __init__(self, job_id_extensions: Optional[Dict[str, str]] = None):
        self.job_id_extensions = JobIdExtension(job_id_extensions)
        self.not_parallelizable_func = (
            'filter_bands',
            'filter_bbox',
            'filter_temporal',
            'array_element'
        )

    def get_domain(self,
                   job_id: str,
                   user_name: str,
                   dags_folder: str,
                   process_graph_json: Union[str, dict],
                   job_data: str,
                   process_defs: Union[dict, list, str],
                   in_filepaths: Dict,
                   wekeo_storage: str = "",
                   user_email: str = None,
                   job_description: str = None,
                   parallelize_tasks: bool = False,
                   vrt_only: bool = False,
                   add_delete_sensor: bool = False,
                   add_parallel_sensor: bool = False
                   ) -> AirflowDagDomain:
        return AirflowDagDomain(job_id=job_id,
                                job_id_extension=self.job_id_extensions,
                                user_name=user_name,
                                dags_folder=dags_folder,
                                process_graph_json=process_graph_json,
                                job_data=job_data,
                                process_defs=process_defs,
                                in_filepaths=in_filepaths,
                                wekeo_storage=wekeo_storage,
                                user_email=user_email,
                                job_description=job_description,
                                parallelize_tasks=parallelize_tasks,
                                vrt_only=vrt_only,
                                add_delete_sensor=add_delete_sensor,
                                add_parallel_sensor=add_parallel_sensor,
                                )

    def write_job(self, job_id: str, user_name: str, dags_folder: str, process_graph_json: Union[str, dict], job_data: str,
                  process_defs: Union[dict, list, str], in_filepaths: Dict, wekeo_storage: str = "",
                  user_email: str = None, job_description: str = None, parallelize_tasks: bool = False,
                  vrt_only: bool = False, add_delete_sensor: bool = False, add_parallel_sensor: bool = False):
        return super().write_job(job_id=job_id, user_name=user_name, dags_folder=dags_folder, process_graph_json=process_graph_json,
                                 job_data=job_data, process_defs=process_defs, in_filepaths=in_filepaths,
                                 wekeo_storage=wekeo_storage, user_email=user_email, job_description=job_description,
                                 parallelize_tasks=parallelize_tasks, vrt_only=vrt_only,
                                 add_delete_sensor=add_delete_sensor, add_parallel_sensor=add_parallel_sensor)

    def move_dag(self, filepath: str, dags_folder: str):
        # Move file to DAGs folder (must copy/delete because of different volume mounts)
        #copyfile(filepath, os.environ.get('AIRFLOW_DAGS') + "/" + filepath)
        copyfile(filepath, dags_folder + "/" + filepath)
        os.remove(filepath)

    def write_and_move_job(self, job_id: str, user_name: str, dags_folder: str, process_graph_json: Union[str, dict], job_data: str,
                           process_defs: Union[dict, list, str], in_filepaths: Dict, wekeo_storage: str = "",
                           user_email: str = None, job_description: str = None, parallelize_tasks: bool = False,
                           vrt_only: bool = False, add_delete_sensor: bool = False, add_parallel_sensor: bool = False):
        _, domain = self.write_job(job_id, user_name, dags_folder, process_graph_json, job_data, process_defs, in_filepaths,
                                   wekeo_storage, user_email, job_description,
                                   parallelize_tasks, vrt_only, add_delete_sensor, add_parallel_sensor)
        self.move_dag(domain.filepath, domain.dags_folder)

    def rewrite_and_move_job(self, domain: AirflowDagDomain):
        _, domain = self.rewrite_job(domain)
        self.move_dag(domain.filepath, domain.dags_folder)

    def get_imports(self, domain: AirflowDagDomain) -> str:
        imports = '''\
from datetime import datetime, timedelta
from airflow import DAG
'''
        if domain.wekeo_storage:
            imports += 'from airflow.hooks.base_hook import BaseHook\n'
        imports += 'from eodatareaders.eo_data_reader import EODataProcessor\n'

        imports2 = 'from airflow.operators import PythonOperator'
        if domain.add_delete_sensor:
            imports2 += ', CancelOp, StopDagOp'
        if domain.add_parallel_sensor:
            imports2 += ', TriggerDagRunOperator'
            imports2 += '\nfrom eodc_openeo_bindings.job_writer.dag_writer import AirflowDagWriter'
            imports2 += '\nfrom time import sleep'
        
        imports += imports2 + '\n'
        
        return imports

    def get_additional_header(self, domain: AirflowDagDomain):
        # dag default args and dag instance
        # some params (e.g. schedule_interval or max_active_runs MUST be set directly as params in DAG to work)
        return f'''\
default_args = {{
    'owner': "{domain.user_name}",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "{domain.user_email}",
    'email_on_failure': False,
    'email_on_retry': False,
}}

dag = DAG(dag_id="{domain.dag_id}",
          description="{domain.job_description}",
          catchup=True,
          max_active_runs=1,
          schedule_interval=None,
          default_args=default_args)
'''

    def get_eodatareaders_task_txt(self, task_id, filepaths, dc_filepaths, process_graph, quotes, queue: str = 'process'):
        
        op_kwargs = {
            'filepaths': filepaths,
            'dc_filepaths': dc_filepaths,
            'user_params': process_graph
        }
        
        return f'''\
{task_id} = PythonOperator(task_id='{task_id}',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={op_kwargs},
                        queue='{queue}'
                        )

'''

    def get_dependencies_txt(self, node_id, dependencies):
        return f'''\
{node_id}.set_upstream([{",".join(map(str, dependencies))}])

'''

    def _get_node_info(self, node, domain):
        node_id = node[0]
        params = node[1]
        node_dependencies = node[2]

        filepaths = None
        n_id = node_id[:node_id.rfind('_')]
        if n_id in domain.in_filepaths:
            # TODO update to: "if node_id in domain.in_filepaths:"
            # when this issue is solved:
            # https://github.com/Open-EO/openeo-pg-parser-python/issues/26
            filepaths = deepcopy(domain.in_filepaths[n_id]['filepaths'])
            if 'wekeo_job_id' in domain.in_filepaths[n_id]:
                # Modify path to file
                for k, item in enumerate(filepaths):
                    filepaths[k] = os.path.join(domain.wekeo_storage, item.split('/')[-1] + ".nc")

        return node_id, params, filepaths, node_dependencies

    def _check_key_is_parallelizable(self, params: List[dict]):
        """
        Flag if current node can be parallelized.
        """
        # TODO we need better logic to decide when a node can be parallelised or not
        for item in params:
            if item['name'] == 'reduce' and item['dimension'] == 'time':
                return False
            elif item['name'] in self.not_parallelizable_func:
                return False
            elif 'f_input' in item:
                if item['f_input']['f_name'] in self.not_parallelizable_func:
                    return False
        
        return True

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
                    print('somethign wrong here.')
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

    def get_nodes(self, domain: AirflowDagDomain) -> Tuple[dict, list]:
        if not domain.nodes:
            domain.nodes, _ = openeo_to_eodatareaders(domain.process_graph_json, domain.job_data, domain.process_defs, vrt_only=domain.vrt_only)
        else:
            existing_nodes = []
            for item in domain.nodes:
                existing_nodes.append(item[0])
            domain.nodes, _ = openeo_to_eodatareaders(domain.process_graph_json, domain.job_data, domain.process_defs, vrt_only=domain.vrt_only,
                                                      existing_node_ids=existing_nodes)

        # Add nodes
        parallel_nodes = {}
        dep_subnodes = {}
        translated_nodes = {}
        for node in domain.nodes:
            node_id, params, filepaths, node_dependencies = self._get_node_info(node, domain)

            # Check node can be parallelized if requested
            parallel_node = False
            if domain.parallelize_task:
                parallel_node = self._check_key_is_parallelizable(params)

            if parallel_node:
                dc_filepaths = None
                filepaths = self.utils.get_filepaths_from_dependencies(node_dependencies, domain.job_data, parallelize=parallel_node)
                dep_subnodes[node_id] = []
                N_deps = len(filepaths)
                N_files = len(filepaths[0])
                for counter_1 in range(N_files):
                    in_files = []
                    for counter_2 in range(N_deps):
                        in_files.append(filepaths[counter_2][counter_1])
                    node_sub_id = node_id + '_' + str(counter_1 + 1)
                    quotes = "" if isinstance(in_files, list) else "'"
                    translated_nodes[node_sub_id] = self.get_eodatareaders_task_txt(task_id=node_sub_id, filepaths=in_files, dc_filepaths=dc_filepaths, process_graph=params, quotes=quotes)
                    dep_subnodes[node_id].append(node_sub_id)
            else:
                dc_filepaths = self.utils.get_dc_filepaths_from_dependencies(node_dependencies, domain.job_data)
                translated_nodes[node_id] = self.get_eodatareaders_task_txt(task_id=node_id, filepaths=filepaths, dc_filepaths=dc_filepaths,
                                                                            process_graph=params, quotes="")
            parallel_nodes[node_id] = parallel_node

        # Add node dependencies
        for node in domain.nodes:
            node_id, params, _, node_dependencies = self._get_node_info(node, domain)

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

    def get_additional_nodes(self, domain: AirflowDagDomain, nodes: List = []) -> Optional[Tuple[dict, list]]:

        additional_nodes = {}
        if domain.add_delete_sensor:
            additional_nodes = self.get_delete_sensor_txt(domain)
        if domain.add_parallel_sensor:
            parallel_nodes = self.get_parallel_dag_txt(domain)
            if additional_nodes:
                additional_nodes = {**additional_nodes, **parallel_nodes}
            else:
                additional_nodes = parallel_nodes
        wekeo_nodes = self.get_wekeo_text(domain, nodes)
        if wekeo_nodes:
            additional_nodes = {**additional_nodes, **wekeo_nodes}
        return additional_nodes

    def get_delete_sensor_txt(self, domain: AirflowDagDomain) -> Tuple[dict, list]:
        nodes = {
            "cancel_sensor": f'''
cancel_sensor = CancelOp(task_id='cancel_sensor',
                         dag=dag,
                         stop_file='{domain.job_data}/STOP',
                         queue='sensor',
                         )
''',
            "stop_dag": f'''
stop_dag = StopDagOp(task_id='stop_dag', dag=dag, queue='process')
''',
            "dep_cancel_action": self.get_dependencies_txt("stop_dag", ["cancel_sensor"]),
        }
        return nodes

    def get_parallel_dag_txt(self, domain: AirflowDagDomain) -> Tuple[dict, list]:
        
        if isinstance(domain.process_graph_json, str):
            domain.process_graph_json = json.load(open(domain.process_graph_json))
        
        op_kwargs={
            'job_id': domain.job_id,
            'user_name': domain.user_name,
            'dags_folder': domain.dags_folder,
            'wekeo_storage': domain.wekeo_storage,
            'process_graph_json': domain.process_graph_json,
            'job_data': domain.job_data,
            'process_defs': domain.process_defs,
            'in_filepaths': domain.in_filepaths
            }

        nodes = {
            "parallel_func": f'''
def parallelise_dag(job_id, user_name, process_graph_json, job_data, process_defs):
    """
    
    """
    
    writer = AirflowDagWriter()
    domain = writer.get_domain(job_id=job_id,
                               user_name=user_name,
                               process_graph_json=process_graph_json,
                               job_data=job_data,
                               process_defs=process_defs,
                               add_delete_sensor=True,
                               vrt_only=False,
                               parallelize_tasks=True)
    domain.job_id = "{self.job_id_extensions.get_parallel(domain.job_id)}"
    writer.rewrite_and_move_job(domain)
    sleep(10)  # give a few seconds to Airflow to add DAG to its internal DB
''',
            "parallel_op": f'''
parallelise_dag = PythonOperator(task_id='parallelise_dag',
                                 dag=dag,
                                 python_callable=parallelise_dag,
                                 op_kwargs = {op_kwargs},
                                 queue='process')
''',
            "dep_parallel_op": self.get_dependencies_txt("parallelise_dag", [domain.nodes[-1][0]]),
            "trigger_new_dag": f'''
trigger_dag = TriggerDagRunOperator(task_id='trigger_dag',
                                   dag=dag,
                                   trigger_dag_id='{self.job_id_extensions.get_parallel(domain.job_id)}',
                                   queue='process')
''',
            "dep_trigger_new_dag": self.get_dependencies_txt("trigger_dag", ["parallelise_dag"]),
        }
        return nodes
    
    def get_wekeo_text(self, domain: AirflowDagDomain, nodes: List) -> Tuple[dict, list]:
        """ """

        # order_id = '{order_id}'
        # headers = {
        #         "Authorization": '"Bearer " + access_token',
        #         "Accept": "application/json"
        #     }
        # job_id_dict = {"jobId": "wekeo_job_id", "uri": "item_url"}
        dag_nodes = {
            "wekeo_func": f'''
def download_wekeo_data(wekeo_job_id, item_url, output_filepath):

    import os
    import requests
    import zipfile

    output_filepath_zip = output_filepath + ".zip"
    output_filepath_nc = output_filepath + ".nc"
    f_name = os.path.basename(output_filepath)
    f_dir = os.path.dirname(output_filepath)

    # Get token
    response = requests.get(BaseHook.get_connection('wekeo_hda').host + "/gettoken",
                            auth=(BaseHook.get_connection("wekeo_hda").login,
                                  BaseHook.get_connection("wekeo_hda").password
                            )
                )
    if not response.ok:
        raise Exception(response.text)
    access_token = response.json()["access_token"]
    service_headers = {{
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        }}
    # Create a WEkEO dataorder
    response2 = requests.post(BaseHook.get_connection('wekeo_hda').host + "/dataorder",
                              json={{"jobId": wekeo_job_id, "uri": item_url}},
                              headers=service_headers)
    if not response2.ok:
        raise Exception(response2.text)
    # check dataorder status
    order_id = response2.json()["orderId"]
    while not response2.json()["message"]:
        response2 = requests.get(BaseHook.get_connection('wekeo_hda').host + "/dataorder/status/" + order_id,
                                 headers=service_headers)
    if not os.path.isfile(output_filepath_nc):
        # Download file
        response3 = requests.get(BaseHook.get_connection('wekeo_hda').host + "/dataorder/download/" + order_id,
                                 headers=service_headers, stream=True)
        if not response3.ok:
            raise Exception(response3.text)
        with open(output_filepath_zip, "wb") as f:
            for chunk in response3.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        # Unzip file
        with zipfile.ZipFile(output_filepath_zip,"r") as zip_ref:
            zip_ref.extractall(f_dir)
        # Move extracted files 'one folder up'
        os.rename(os.path.join(output_filepath, f_name + ".nc"), os.path.join(f_dir, f_name + ".nc"))
        os.rename(os.path.join(output_filepath, f_name + ".cdl"), os.path.join(f_dir, f_name + ".cdl"))
        # Remove zip file and empty folder
        os.remove(output_filepath_zip)
        os.rmdir(output_filepath)
'''
        }

        return_nodes = False
        for item in domain.in_filepaths:
            if 'wekeo_job_id' in domain.in_filepaths[item]:
                for k, item_url in enumerate(domain.in_filepaths[item]['filepaths']):
                    return_nodes = True
                    op_kwargs = {
                        'wekeo_job_id': domain.in_filepaths[item]['wekeo_job_id'],
                        'item_url': item_url,
                        'output_filepath': os.path.join(domain.wekeo_storage, item_url.split('/')[1])
                        }
                    # TODO remove when this issue with pg-parser is fixed:
                    # https://github.com/Open-EO/openeo-pg-parser-python/issues/26
                    for node_id in nodes:
                        if item in node_id:
                            child_node_id = node_id
                    ###
                    dag_nodes[f"wekeo_{k}"] = f'''
wekeo_{k} = PythonOperator(task_id='wekeo_download_{k}',
                                 dag=dag,
                                 python_callable=download_wekeo_data,
                                 op_kwargs = {op_kwargs},
                                 queue='process')
wekeo_{k}.set_downstream([{child_node_id}])
    '''

        if return_nodes:
            return dag_nodes
        else:
            return ({})
