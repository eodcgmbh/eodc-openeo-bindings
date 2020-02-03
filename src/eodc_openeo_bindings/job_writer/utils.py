import glob
import os
from typing import Union, List


class JobWriterUtils:

    def get_file_list(self, filepaths: Union[str, list]) -> str:
        if isinstance(filepaths, str):
            file_list = f'''\
filepaths = sorted(glob.glob('{filepaths}' + '/*'))'''

        elif isinstance(filepaths, list):
            file_list = f'''\
input_filepaths = {filepaths}
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))'''

        else:
            raise Exception(f'Filepaths of type {type(filepaths)} are not supported!')

        return file_list

    def get_existing_node(self, job_folder: str, node_ids: list) -> list:
        """
        Get matching node discarding the hash.
        """
        if not (os.path.isdir(job_folder) and node_ids):
            return node_ids

        if not isinstance(node_ids, list):
            node_ids = [node_ids]

        subfolders = glob.glob(job_folder + '/*')  # TODO check if os.listdir can do the same
        for folder in subfolders:
            for k, node_id in enumerate(node_ids):
                if (node_id.split('_')[0] + '_') in folder.split('/')[-1]:
                    node_ids[k] = folder.split('/')[-1]

        return node_ids

    def check_params_key(self, params: List[dict], key_name: str, key_value=None):
        key_name_exists = False
        value_name_matches = False

        index = None
        for k, item in enumerate(params):
            if key_name in item.keys():
                key_name_exists = True
                if key_value and item[key_name] == key_value:
                    value_name_matches = True
            index = k

        # double check that process is indeed parallelizable > TODO separate!
        return key_name_exists, value_name_matches, index

    def get_input_paths(self, node_dependencies, job_data, parallelize):
        """
        Create filepaths as a list of folders or list of files
        """

        node_dependencies_path = []
        for dep in node_dependencies:
            dep_path = os.path.join(job_data, dep)
            if not os.path.isdir(dep_path):
                dep_path = job_data + os.path.sep + dep + os.path.sep
            node_dependencies_path.append(dep_path)

        filepaths = []
        if parallelize:
            counter = 0
            while counter >= 0:
                counter += 1
                paths_tmp = []
                for k, _ in enumerate(node_dependencies_path):
                    paths_tmp.extend(
                        glob.glob(node_dependencies_path[k] + '/*_*_*_{value}_*'.format(value=str(counter))))
                if paths_tmp:
                    filepaths.append(paths_tmp)
                else:
                    counter = -1
        else:
            for item in node_dependencies_path:
                if os.path.isdir(item):
                    filepaths.extend(glob.glob(item + '/*'))
                else:
                    filepaths.append(item)

        return filepaths
