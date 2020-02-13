from abc import ABC, abstractmethod
from typing import Optional, Union, Tuple

from eodc_openeo_bindings.job_writer.utils import JobWriterUtils


class JobWriter(ABC):

    utils = JobWriterUtils()

    def __init__(self, process_graph_json: Union[str, dict], job_data, file_handler, output_filepath: str = None):

        self.file_handler = file_handler(self.get_filepath(output_filepath))
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

    def write_job(self):
        self.file_handler.open()
        self.file_handler.append(self.get_imports())
        self.file_handler.append('\n')

        additional_header = self.get_additional_header()
        if additional_header:
            self.file_handler.append(additional_header)
            self.file_handler.append('\n')

        nodes, ordered_keys = self.get_nodes()
        for node_id in ordered_keys:
            self.file_handler.append(nodes[node_id])

        self.file_handler.close()
        return self.output_format, self.output_folder

    @abstractmethod
    def get_imports(self) -> str:
        pass

    def get_additional_header(self) -> Optional[str]:
        return None

    @abstractmethod
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
                    # TODO check this is working!
                    self.output_format = item['name']['format']
                else:
                    self.output_format = 'Gtiff'