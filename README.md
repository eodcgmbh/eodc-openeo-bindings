# eodc-openeo-bindings

This package contains classes and functions to convert a job from the openEO syntax to an Apache Airflow DAG or basic
Python script, both relying on eoDataReaders for data processing.

## Installation

Conda:
```
conda env create -f conda_environment.yml
python setup.py install
```

Virtualenv
```
virtualenv eodc-openeo-bindings -p python3.6
source activate eodc-openeo-bindings
python setup.py install
```
In case you want to run tests also run
```
pip install -r requirements-test.txt
```


## Run tests

Important: currently the tests rely on having a local CSW server set up as described in
https://github.com/Open-EO/openeo-openshift-driver/tree/master/csw

To execute the tests (Make sure you installed the test requirements - see section above):
`python setp.py test`

## Examples

Create Apache Airflow DAG file (naming: `dag_<job_id>.py` - `_parallelized` is added to the end of the name if the dag
is to be run in parallel):
```python
from eodc_openeo_bindings.job_writer.dag_writer import AirflowDagWriter

writer = AirflowDagWriter()  # class can be initiated before usage and can then be reused multiple times
# the ProcessGraphJson can be either a dictionary or a path to a ProcessGraph json-file
writer.write_and_move_job(job_id="job-1234", user_name="test-user", process_graph_json={}, job_data="/path/to/job/folder")
```

Create Python script:
```python
from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter

writer = BasicJobWriter()
writer.write_job(process_graph_json="/path/to/process_graph.json", job_data="/path/to/job/folder")
```


### Note

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
