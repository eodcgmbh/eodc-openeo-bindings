import os
from eodc_openeo_bindings.write_jupyter_nb import write_jupyter_nb


os.environ['CSW_SERVER'] = 'https://csw.eodc.eu'
FOLDER = os.path.join(os.getcwd(), 'tests')

evi_file = os.path.join(FOLDER, 'process_graphs/evi.json')
out_filepath = os.path.join(FOLDER, "openeo_job.ipynb")
job_data = os.path.join(FOLDER, 'openeo_job')

write_jupyter_nb(evi_file, job_data, nb_filepath=out_filepath)
