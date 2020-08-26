"""
This test checks the input file generation of a airflow dag job.
"""


import os
from shutil import copytree, rmtree
from eodc_openeo_bindings.job_writer.dag_writer import AirflowDagWriter


def get_ref_node_from_name(name, all_nodes):
    cur_ref_index = [i for i, node in enumerate(all_nodes) if node.name == name][0]
    return all_nodes[cur_ref_index]


def test_airflow_dag(csw_server, test_folder, evi_file, 
                     setup_airflow_dag_folder, setup_ref_job_folder, backend_processes):

    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-12345"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, process_graph_json=evi_file, job_data=job_data,
                              process_defs=backend_processes)

    with open(out_filepath) as outfile:
        out_content = outfile.read()
    
    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(os.environ['AIRFLOW_DAGS'], os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    
    assert out_content == ref_content


def test_airflow_dag_vrt_only(csw_server, test_folder, evi_file, 
                              setup_airflow_dag_folder, setup_ref_job_folder, backend_processes):
    
    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-12346"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, process_graph_json=evi_file, job_data=job_data,
                              process_defs=backend_processes, vrt_only=True)

    with open(out_filepath) as outfile:
        out_content = outfile.read()
    
    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(os.environ['AIRFLOW_DAGS'], os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    
    assert out_content == ref_content


def test_airflow_dag_parallel(csw_server, test_folder, evi_file, setup_airflow_dag_folder, airflow_job_folder, 
                              setup_ref_job_folder, backend_processes):

    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-12345"
    user_name = "jdoe_67890"
    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, process_graph_json=evi_file, job_data=job_data,
                              process_defs=backend_processes, vrt_only=True)

    # Simulate that job has ran (place vrt files in node folders)
    copytree(airflow_job_folder, job_data)
    # Recreate (parallelised DAG)
    writer = AirflowDagWriter()
    domain = writer.get_domain(job_id, user_name, evi_file, job_data, process_defs=backend_processes, vrt_only=False, parallelize_tasks=True)
    domain.job_id = domain.job_id + "_2"
    # (Re)write DAG, now parallelised
    writer.rewrite_and_move_job(domain)
    
    rmtree(os.path.join(test_folder, 'openeo_job'))
    
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '_parallelize.py')

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(os.environ['AIRFLOW_DAGS'], os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_airflow_dag_delete_sensor(csw_server, test_folder, evi_file, setup_airflow_dag_folder, 
                                   setup_ref_job_folder, backend_processes):

    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-12345_delete_sensor"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, process_graph_json=evi_file, job_data=job_data,
                              process_defs=backend_processes, add_delete_sensor=True)

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(os.environ['AIRFLOW_DAGS'], os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    assert out_content == ref_content
