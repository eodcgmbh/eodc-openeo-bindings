# eodc-openeo-bindings

This package contains classes and functions to convert a job from the openEO syntax to an Apache Airflow DAG or basic Python script, both relying on eoDataReaders for data processing.

## Installation

```
conda env create -f conda_environment.yml
python setup.py install
```

## Run tests

Important: currently the tests rely on having a local CSW server set up as described in https://github.com/Open-EO/openeo-openshift-driver/tree/master/csw

`python setp.py test`

## Examples

Create Apache Airflow DAG file:

`AirflowDagWriter("dag_id", "username", "pg_evi.json", "data_output_folder").write_and_move_job()`

Create Python script:

`BasicJobWriter("pg_evi.json", "data_output_folder", "my_script.py").write_job()`




### Note

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
