"""
This test checks the input file generation of a airflow dag job.
"""


import os
from shutil import copytree, rmtree
from eodc_openeo_bindings.job_writer.dag_writer import AirflowDagWriter


def get_ref_node_from_name(name, all_nodes):
    cur_ref_index = [i for i, node in enumerate(all_nodes) if node.name == name][0]
    return all_nodes[cur_ref_index]


def test_airflow_dag(csw_server, test_folder, evi_file, evi_ref_node, 
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

    job_id = "jb-12345_parallelised"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter()
    writer.write_and_move_job(job_id=job_id, user_name=user_name, process_graph_json=evi_file, job_data=job_data,
                              process_defs=backend_processes, vrt_only=True)
    
    # Simulate that job has ran (place vrt files in node folders)
    domain = writer.get_domain(job_id, user_name, evi_file, job_data, process_defs=backend_processes, vrt_only=True)
    _, node_ids = writer.get_nodes(domain)
    ref_node_ids = ['blue', 'dc', 'div', 'evi', 'min', 'mintime', 'nir', 'p1', 'p2', 'p3', 'red', 'save', 'sub', 'sum']
    for node_id in node_ids:
        node_folder = os.path.join(job_data, node_id)
        for ref_node_id in ref_node_ids:
            if ref_node_id == node_id.split('_')[0]:
                copytree(os.path.join(airflow_job_folder, ref_node_id), node_folder)
    
    # (Re)write DAG, now parallelised
    domain.vrt_only = False
    domain.parallelize_task = True
    writer.rewrite_and_move_job(domain)
    
    with open(out_filepath) as outfile:
        out_content = outfile.read()
    
    ref_filepath = out_filepath.replace('.py', '_ref.py').replace(os.environ['AIRFLOW_DAGS'], os.environ['REF_JOBS'])
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    
    assert out_content == ref_content
    
    rmtree(os.path.join(test_folder, 'openeo_job'))


def test_airflow_dag_delete_sensor(csw_server, test_folder, evi_file, evi_ref_node, setup_airflow_dag_folder, 
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
