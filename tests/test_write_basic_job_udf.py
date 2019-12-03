"""

"""


import os
from eodc_openeo_bindings.write_basic_job import write_basic_job


os.environ['CSW_SERVER'] = 'https://csw.eodc.eu'
FOLDER = os.path.join(os.getcwd(), 'tests')

evi_file = os.path.join(FOLDER, 'process_graphs/udf_example.json')
job_data = os.path.join(FOLDER, 'basic_job')
out_filepath = os.path.join(FOLDER, "basic_job.py")

output_format, output_folder = write_basic_job(evi_file, job_data, python_filepath=out_filepath)
import pdb; pdb.set_trace()
assert output_format == 'Gtiff'
assert 'save' in output_folder
