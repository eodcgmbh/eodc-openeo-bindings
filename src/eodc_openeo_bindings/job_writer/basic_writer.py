import os
from typing import Union, Tuple

from eodc_openeo_bindings.job_writer.job_domain import BasicJobDomain
from eodc_openeo_bindings.job_writer.job_writer import JobWriter
from eodc_openeo_bindings.openeo_to_eodatareaders import openeo_to_eodatareaders


class BasicJobWriter(JobWriter):

    def write_job(self, process_graph_json: Union[str, dict], job_data: str, 
                  process_defs: Union[dict, list, str], output_filepath: str = None):
        return super().write_job(process_graph_json=process_graph_json, job_data=job_data,
                                 process_defs=process_defs, output_filepath=output_filepath)

    def get_domain(self, process_graph_json: Union[str, dict], job_data: str, 
                   process_defs: Union[dict, list, str], output_filepath: str = None):
        return BasicJobDomain(process_graph_json, job_data, process_defs, output_filepath)

    def get_imports(self, domain) -> str:
        return '''\
import glob
from eodatareaders.eo_data_reader import eoDataReader
'''

    def get_node_txt(self, node_id, params, filepaths, filepaths0, node_operator):
        return f'''\
### {node_id} ###
# node input files
{filepaths0}{filepaths}

# node input parameters
params = {params}

# evaluate node
{node_id} = {node_operator}(filepaths, params)

'''

    def get_nodes(self, domain: BasicJobDomain) -> Tuple[dict, list]:
        nodes, graph = openeo_to_eodatareaders(domain.process_graph_json, domain.job_data, domain.process_defs)

        translated_nodes = {}
        translated_nodes_keys = []
        for node in nodes:
            node_id = node[0]
            params = node[1]
            filepaths = node[2]
            node_dependencies = node[3]
            node_operator = node[4]

            if filepaths:
                filepaths0 = 'filepaths = '
            else:
                if not node_dependencies:
                    raise Exception(f'No filepaths and no node dependencies for node: {node_id}')

                filepaths0 = ''
                filepaths = []
                for dep in node_dependencies:
                    filepaths.append(domain.job_data + os.path.sep + dep + os.path.sep)
                filepaths = self.utils.get_file_list(filepaths)

            translated_nodes[node_id] = self.get_node_txt(node_id=node_id, params=params, filepaths=filepaths,
                                                          filepaths0=filepaths0, node_operator=node_operator)
            translated_nodes_keys.append(node_id)

        for node in nodes:
            node_id = node[0]
            node_dependencies = node[3]

            current_index = translated_nodes_keys.index(node_id)
            dep_indices = []
            if node_dependencies:
                for dep in node_dependencies:
                    dep_indices.append(translated_nodes_keys.index(dep))
            else:
                dep_indices.append(0)

            this_node = translated_nodes_keys.pop(current_index)
            translated_nodes_keys.insert(max(dep_indices) + 1, this_node)

        return translated_nodes, translated_nodes_keys
