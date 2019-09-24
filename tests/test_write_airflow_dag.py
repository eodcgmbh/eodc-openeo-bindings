"""

"""


import os
from eodc_openeo_bindings.write_airflow_dag import write_airflow_dag


FOLDER = os.path.join(os.getcwd(), 'tests')
os.environ['CSW_SERVER'] = 'https://csw.eodc.eu'
os.environ['AIRFLOW_DAGS'] = FOLDER

evi_file = os.path.join(FOLDER, 'process_graphs/evi.json')
job_data = os.path.join(FOLDER, 'openeo_job')

job_id = "jb-12345"
user_name = "jdoe_67890"

write_airflow_dag(job_id, user_name, process_graph_json=evi_file, job_data=job_data)
