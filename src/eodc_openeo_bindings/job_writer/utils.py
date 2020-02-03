import glob
import os
from typing import Union


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

    def get_existing_node(self, job_folder: str, target_ids: list) -> list:
        """
        Get matching node discarding the hash.
        """
        if not (os.path.isdir(job_folder) and target_ids):
            return target_ids

        if not isinstance(target_ids, list):
            target_ids = [target_ids]

        subfolders = glob.glob(job_folder + '/*')  # TODO check if os.listdir can do the same
        for folder in subfolders:
            for k, node_id in enumerate(target_ids):
                if (node_id.split('_')[0] + '_') in folder.split('/')[-1]:
                    target_ids[k] = folder.split('/')[-1]

        return target_ids

    def check_params_key(self, params, key_name, key_value=None):
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
