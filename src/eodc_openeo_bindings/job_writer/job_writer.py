from typing import Optional, Union, Tuple


class JobWriterUtils:

    def get_file_list(self, filepaths: Union[str, list]) -> str:
        if isinstance(filepaths, str):
            file_list = f'''\
filepaths = sorted(glob.glob('{filepaths}' + '/*'))'''

        elif isinstance(filepaths, list):
            file_list = f'''\
input_filepaths = {filepaths}
filepaths = []
for path in {filepaths}:
    filepaths.extend(sorted(glob.glob(path + '/*')))'''

        else:
            raise Exception(f'Filepaths of type {type(filepaths)} are not supported!')

        return file_list


class JobWriter:

    utils = JobWriterUtils()

    def __init__(self, process_graph_json: Union[str, dict], job_data, filepath: str = None):
        self.filepath = self.get_filepath(filepath)
        self.process_graph_json = process_graph_json
        self.job_data = job_data

        self.output_folder = None
        self.output_format = None

    def get_filepath(self, filepath: str) -> str:
        if not filepath:
            return self.get_default_filepath()
        return filepath

    def get_default_filepath(self) -> str:
        pass

    def open_job(self):
        pass

    def append_to_job(self, job, content):
        pass

    def close_job(self, job):
        pass

    def write_job(self):
        job = self.open_job()
        job = self.append_to_job(job, self.get_imports())
        job = self.append_to_job(job, '\n')

        additional_header = self.get_additional_header()
        if additional_header:
            job = self.append_to_job(job, additional_header)
            job = self.append_to_job(job, '\n')

        nodes, ordered_keys = self.get_nodes()
        for node_id in ordered_keys:
            job = self.append_to_job(job, nodes[node_id])

        self.close_job(job)

    def get_imports(self) -> str:
        pass

    def get_additional_header(self) -> Optional[str]:
        return None

    def get_nodes(self) -> Tuple[dict, list]:
        # Needs to call set_output_format_and_folder
        pass

    def set_output_format_and_folder(self, node):
        params = node[1]

        for item in params:
            if item['name'] == 'set_output_folder':
                self.output_folder = item['folder_name']
            if item['name'] == 'save_raster':
                if 'format' in item.keys():
                    self.output_format = item['name']['format']
                else:
                    self.output_format = 'Gtiff'
