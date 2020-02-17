"""

"""


import os
from eodc_openeo_bindings.write_basic_job import write_basic_job


os.environ['CSW_SERVER'] = 'http://127.0.0.1:8000/'
FOLDER = os.path.join(os.getcwd(), 'tests')

evi_file = os.path.join(FOLDER, 'process_graphs/udf_python.json')
job_data = os.path.join(FOLDER, 'output_udf_python')
out_filepath = os.path.join(FOLDER, "basic_udf_python.py")

output_format, output_folder = write_basic_job(evi_file, job_data, python_filepath=out_filepath)
assert output_format == 'Gtiff'
assert 'udf' in output_folder
