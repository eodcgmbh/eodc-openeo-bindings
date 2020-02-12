from typing import Union

from eodc_openeo_bindings.job_writer.simple_job_writer import SimpleJobWriter
from eodc_openeo_bindings.job_writer.file_handler import JupyterNotebookFileHandler


class JupyterNotebookWriter(SimpleJobWriter):

    def __init__(self, process_graph_json: Union[str, dict], job_data, output_filepath: str = None):
        super().__init__(process_graph_json, job_data, JupyterNotebookFileHandler, output_filepath)

    def get_default_filepath(self) -> str:
        return 'test.ipynb'

