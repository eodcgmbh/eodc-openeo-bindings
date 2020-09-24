"""
This test checks the input file generation of a airflow dag job.
"""


import os
from shutil import copytree, rmtree

from eodc_openeo_bindings.job_writer.dag_writer import AirflowDagWriter


def get_ref_node_from_name(name, all_nodes):
    cur_ref_index = [i for i, node in enumerate(all_nodes) if node.name == name][0]
    return all_nodes[cur_ref_index]


def test_airflow_dag(evi_file,
                     airflow_dag_folder, setup_ref_job_folder,
                     backend_processes, S2_filepaths):

    job_id = "jb-12345"
    out_filepath = os.path.join(airflow_dag_folder, f'dag_{job_id}_prep.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, dags_folder=airflow_dag_folder, process_graph_json=evi_file, job_data='./openeo_job',
                              process_defs=backend_processes, in_filepaths=S2_filepaths)

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(airflow_dag_folder, os.environ['REF_JOBS'])
    with open(ref_filepath) as ref_file:
        ref_content = ref_file.read()

    assert out_content == ref_content


def test_airflow_dag_vrt_only(evi_file,
                              airflow_dag_folder, setup_ref_job_folder,
                              backend_processes, S2_filepaths):

    job_id = "jb-12346"
    out_filepath = os.path.join(airflow_dag_folder, f'dag_{job_id}_prep.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, dags_folder=airflow_dag_folder, process_graph_json=evi_file, job_data='./openeo_job',
                              process_defs=backend_processes, in_filepaths=S2_filepaths, vrt_only=True)

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(airflow_dag_folder, os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_airflow_dag_parallel(evi_file, airflow_dag_folder, airflow_job_folder,
                              setup_ref_job_folder, backend_processes, S2_filepaths):

    job_data = './openeo_job'

    job_id = "jb-12347"
    user_name = "jdoe_67890"
    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, dags_folder=airflow_dag_folder, process_graph_json=evi_file, job_data=job_data,
                              process_defs=backend_processes, in_filepaths=S2_filepaths,
                              vrt_only=True, add_delete_sensor=True, add_parallel_sensor=True)

    # Check DAG before parallelisation
    out_filepath = os.path.join(airflow_dag_folder, f'dag_{job_id}_prep.py')
    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(airflow_dag_folder, os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    assert out_content == ref_content

    # Simulate that job has ran (place vrt files in node folders)
    if os.path.isdir(job_data):
        rmtree(job_data)
    copytree(airflow_job_folder, job_data)

    # Recreate (parallelised DAG)
    writer = AirflowDagWriter()
    domain = writer.get_domain(job_id, user_name, airflow_dag_folder, evi_file, job_data,
                               process_defs=backend_processes, in_filepaths=S2_filepaths,
                               vrt_only=False, parallelize_tasks=True, add_delete_sensor=True)
    # domain.job_id = domain.job_id + "_2"
    # (Re)write DAG, now parallelised
    writer.rewrite_and_move_job(domain)

    rmtree(job_data)

    # Check DAG after parallelisation
    out_filepath = os.path.join(airflow_dag_folder, f'dag_{job_id}_parallel.py')
    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(airflow_dag_folder, os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    assert out_content == ref_content


def test_airflow_dag_delete_sensor(evi_file, airflow_dag_folder, setup_ref_job_folder,
                                   backend_processes, S2_filepaths):

    job_id = "jb-12345_delete_sensor"
    out_filepath = os.path.join(airflow_dag_folder, f'dag_{job_id}_prep.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, dags_folder=airflow_dag_folder, process_graph_json=evi_file, job_data='./openeo_job',
                              process_defs=backend_processes, in_filepaths=S2_filepaths, add_delete_sensor=True)

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(airflow_dag_folder, os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    assert out_content == ref_content
