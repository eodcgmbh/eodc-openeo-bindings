from typing import Union


class JobDomain:

    def __init__(self):
        self.filepath = self.get_filepath()

    def get_filepath(self) -> str:
        pass


class BasicJobDomain(JobDomain):

    def __init__(self, process_graph_json: Union[str, dict], job_data: str, output_filepath: str = None):
        self.process_graph_json = process_graph_json
        self.job_data = job_data
        self.output_filepath = output_filepath
        super(BasicJobDomain, self).__init__()

    def get_filepath(self) -> str:
        return self.output_filepath if self.output_filepath else 'test.py'


class AirflowDagDomain(JobDomain):

    def __init__(self, job_id: str, user_name: str, process_graph_json: Union[str, dict], job_data: str,
                 user_email: str = None, job_description: str = None, parallelize_tasks: bool = False,
                 vrt_only: bool = False, add_delete_sensor: bool = False):
        self.process_graph_json = process_graph_json
        self.job_data = job_data
        self.job_id = job_id
        self.user_name = user_name
        self.user_email = user_email
        self.job_description = job_description if job_description else 'No description provided'
        self.parallelize_task = parallelize_tasks
        self.vrt_only = vrt_only
        self.add_delete_sensor = add_delete_sensor
        self.nodes = None  # filled if task is parallelised
        super(AirflowDagDomain, self).__init__()

    def get_filepath(self, **kwargs) -> str:
        dag_name = f'dag_{self.job_id}'
        if self.parallelize_task:
            dag_name += '_parallelize'
        return dag_name + '.py'
