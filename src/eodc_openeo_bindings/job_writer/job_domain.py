from typing import List, Union

from eodc_openeo_bindings.job_writer.utils import JobIdExtension


class JobDomain:

    def __init__(self):
        self.filepath = self.get_filepath()

    def get_filepath(self) -> str:
        pass


class BasicJobDomain(JobDomain):

    def __init__(self, process_graph_json: Union[str, dict], job_data: str, 
                 process_defs: Union[dict, list, str], filepaths: List[str],
                 output_filepath: str = None):
        self.process_graph_json = process_graph_json
        self.job_data = job_data
        self.process_defs= process_defs
        self.filepaths = filepaths
        self.output_filepath = output_filepath
        super(BasicJobDomain, self).__init__()

    def get_filepath(self) -> str:
        return self.output_filepath if self.output_filepath else 'test.py'


class AirflowDagDomain(JobDomain):

    def __init__(self,
                 job_id: str,
                 job_id_extension: JobIdExtension,
                 user_name: str,
                 process_graph_json: Union[str, dict],
                 job_data: str,
                 process_defs: Union[dict, list, str],
                 filepaths: List[str],
                 user_email: str = None,
                 job_description: str = None,
                 parallelize_tasks: bool = False,
                 vrt_only: bool = False,
                 add_delete_sensor: bool = False,
                 add_parallel_sensor: bool = False,
                 ):
        """
        Args:
            job_id: The identifier of the job. NOT equivalent to the dag_id.
            job_id_extension: Class storing and adding job_id extnsions.
            user_name: The user name.
            user_email: The user email address.
            process_graph_json: The process graph.
            job_data:
            process_defs:
            job_description: A short description about the job.
            parallelize_tasks: Use existing vrt files and create nodes for parallel tasks.
            vrt_only: Whether the dag should ONLY create vrt files. If activated nothing will be processed only
                description on how to do this will be created. The created vrt files can be used to run the job in
                parallel in a following dag.
            add_delete_sensor: Adds an airflow sensor task to ensure dags can be stopped.
            add_parallel_sensor: Adds a node which will create and trigger a second parallelized dag based on vrt files.
        """
        self.process_graph_json = process_graph_json
        self.job_data = job_data
        self.process_defs = process_defs
        self.filepaths = filepaths
        self.job_id = job_id
        self.job_id_extension = job_id_extension
        self.user_name = user_name
        self.user_email = user_email
        self.job_description = job_description if job_description else 'No description provided'
        self.parallelize_task = parallelize_tasks
        self.vrt_only = vrt_only
        self.add_delete_sensor = add_delete_sensor
        self.add_parallel_sensor = add_parallel_sensor
        self.nodes = None  # filled if task is parallelised
        super(AirflowDagDomain, self).__init__()

    @property
    def dag_id(self):
        """Get the dag-id based on given parameters."""
        if self.parallelize_task:
            return f'{self.job_id_extension.get_parallel(self.job_id)}'
        else:
            return f'{self.job_id_extension.get_preparation(self.job_id)}'

    def get_filepath(self, **kwargs) -> str:
        """Create the name of the dag-file.

        Here dag-filename and dag-id are equal.
        """
        return f'dag_{self.dag_id}.py'
