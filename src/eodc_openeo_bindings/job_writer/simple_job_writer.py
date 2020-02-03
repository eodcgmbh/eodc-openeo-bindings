import os
from typing import Tuple

from eodc_openeo_bindings.job_writer.job_writer import JobWriter
from eodc_openeo_bindings.openeo_to_eodatareaders import openeo_to_eodatareaders


class SimpleJobWriter(JobWriter):

    def get_imports(self) -> str:
        return '''\
    import glob
    from eodatareaders.eo_data_reader import eoDataReader
    '''

    def get_node_txt(self, node_id, params, filepaths, filepaths0):
        return f'''\
### {node_id} ###
# node input files
{filepaths0}{filepaths}

# node input parameters
params = {params}

# evaluate node
{node_id} = eoDataReader(filepaths, params)
    '''

    def get_nodes(self) -> Tuple[dict, list]:
        nodes, graph = openeo_to_eodatareaders(self.process_graph_json, self.job_data)

        translated_nodes = {}
        translated_nodes_keys = []
        for node in nodes:
            node_id = node[0]
            params = node[1]
            filepaths = node[2]
            node_dependencies = node[3]

            if filepaths:
                filepaths0 = 'filepaths = '
            else:
                if not node_dependencies:
                    raise Exception(f'No filepaths and no node dependencies for node:{node_id}')

                filepaths0 = ''
                filepaths = []
                for dep in node_dependencies:
                    filepaths.append(self.job_data + os.path.sep + dep + os.path.sep)
                filepaths = self.utils.get_file_list(filepaths)

            translated_nodes[node_id] = self.get_node_txt(node_id=node_id, params=params, filepaths=filepaths,
                                                          filepaths0=filepaths0)
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

        last_node = [node for node in nodes if node[0] == translated_nodes_keys[-1]][0]
        self.set_output_format_and_folder(last_node)
        return translated_nodes, translated_nodes_keys
