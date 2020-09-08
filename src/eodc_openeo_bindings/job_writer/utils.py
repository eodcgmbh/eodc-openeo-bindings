import glob
import os
from typing import Union, List, Optional, Dict


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
    filepaths.extend(sorted(glob.glob(path + '/*[!.dc]')))'''

        else:
            raise Exception(f'Filepaths of type {type(filepaths)} are not supported!')

        return file_list

    def get_existing_node(self, job_folder: str, node_ids: list) -> list:
        """
        Get matching node discarding the hash.
        """
        
        if not isinstance(node_ids, list):
            node_ids = [node_ids]
            
        if not (os.path.isdir(job_folder) and node_ids):
            return node_ids

        subfolders = glob.glob(job_folder + '/*')
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
        return key_name_exists, value_name_matches, index

    def get_filepaths_from_dependencies(self, node_dependencies, job_data, parallelize):
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
            # Get list of files in node folder, excluding the "pickled" .dc file
            paths_tmp = [sorted(glob.glob(cur_dep_path +  '/*[!.dc]'))
                         for k, cur_dep_path in enumerate(node_dependencies_path)]
            if paths_tmp:
                filepaths.extend(paths_tmp)
        else:
            for k, item in enumerate(node_dependencies_path):
                if os.path.isdir(item):
                    filepaths.extend(glob.glob(item + '/*.dc'))
                else:                    
                    filepaths.append(os.path.join(item, node_dependencies[k] + '.dc'))

        return filepaths
        
    def get_dc_filepaths_from_dependencies(self, node_dependencies, job_data):
        """
        
        """
        
        dc_filepaths = self.get_filepaths_from_dependencies(node_dependencies, job_data, parallelize=False)
        
        if len(dc_filepaths) == 0:
            dc_filepaths = None
        
        return dc_filepaths


class JobIdExtension:

    def __init__(self, extensions: Optional[Dict[str, str]] = None) -> None:
        self.preparation = "prep"
        self.parallel = "parallel"
        if isinstance(extensions, dict):
            if "preparation" in extensions:
                self.preparation = extensions["preparation"]
            if "parallel" in extensions:
                self.parallel = extensions["parallel"]

    def get_preparation(self, job_id: str) -> str:
        return f"{job_id}_{self.preparation}"

    def get_parallel(self, job_id: str) -> str:
        return f"{job_id}_{self.parallel}"
