"""

"""


import os
from eodc_openeo_bindings.write_basic_job import write_basic_job


os.environ['CSW_SERVER'] = 'https://csw.eodc.eu'
FOLDER = os.path.join(os.getcwd(), 'tests')

evi_file = os.path.join(FOLDER, 'process_graphs/evi.json')
job_data = os.path.join(FOLDER, 'basic_job')
out_filepath = os.path.join(FOLDER, "basic_job.py")

write_basic_job(evi_file, job_data, python_filepath=out_filepath)