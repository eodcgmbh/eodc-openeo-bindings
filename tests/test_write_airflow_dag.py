"""
This test checks the input file generation of a airflow dag job.
"""


import os
import re
import glob
from shutil import copytree, rmtree

from eodc_openeo_bindings.job_writer.dag_writer import AirflowDagWriter


def get_ref_node_from_name(name, all_nodes):
    cur_ref_index = [i for i, node in enumerate(all_nodes) if node.name == name][0]
    return all_nodes[cur_ref_index]


def setup_folder(test_folder):
    os.environ['AIRFLOW_DAGS'] = os.path.join(test_folder, 'airflow_dag')
    if not os.path.exists(os.environ['AIRFLOW_DAGS']):
        os.makedirs(os.environ['AIRFLOW_DAGS'])
        

def cleanup(out_filepath):

    os.remove(out_filepath)
    os.rmdir(os.environ['AIRFLOW_DAGS'])


def test_airflow_dag(csw_server, test_folder, evi_file, evi_ref_node):

    setup_folder(test_folder)
        
    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-12345"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter(job_id, user_name, process_graph_json=evi_file, job_data=job_data)
    writer.write_and_move_job()

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'[A-Za-z]*_[A-Za-z0-9]* = ', out_content)[2:]  # Discard header and dag definition
    assert len(actual_nodes) == 14
    actual_relations = actual_nodes[13].split('\n\n')[1:]
    actual_nodes[13] = actual_nodes[13].split('\n\n')[0]

    for actual_node in actual_nodes:
        actual_node_parts = actual_node.split('\n')
        task_id = actual_node_parts[0].strip()
        actual_paths = actual_node_parts[2].strip()
        actual_params = actual_node_parts[3].strip()

        # Check eoDataReadersOp is used
        assert re.match(r"eoDataReadersOp\(task_id='[A-Za-z0-9]*_[A-Za-z0-9]*',", task_id)

        # Get current node
        actual_name = task_id[len("eoDataReadersOp(task_id='"):].split('_')[0]
        cur_ref_node = get_ref_node_from_name(actual_name, evi_ref_node)

        if cur_ref_node.input_filepaths:
            actual_paths = re.search(r'\[.*\]', actual_paths).group()
            actual_paths = actual_paths[2:-2].split("', '")

            # Check number of input filepaths match
            assert len(actual_paths) == len(cur_ref_node.input_filepaths)
            for ref_dep, actual_input_path in zip(cur_ref_node.input_filepaths, actual_paths):
                actual_path_name = actual_input_path.split('/')[-2]
                # Check input path match the correct dependency nodes
                assert actual_path_name.startswith(ref_dep)

        # Only parent folder is checked, but no other parameters
        actual_params = actual_params.split('=')[-1].strip()
        actual_params = eval(actual_params)
        for key, value in actual_params[0].items():
            # Check parent node name
            if key == 'folder_name':
                assert value.split('/')[-2].startswith(cur_ref_node.name)

    # needs to match the before checked input paths!
    actual_relations = [ar for ar in actual_relations if ar != '']
    assert len(actual_relations) == 13

    for actual_relation in actual_relations:
        actual_name = actual_relation.split('_')[0]
        cur_ref_node = get_ref_node_from_name(actual_name, evi_ref_node)
        # Get list of dependencies
        actual_dep = re.search(r'\[.*\]', actual_relation).group()[1:-1]  # get all dependencies and remove []
        actual_dep = actual_dep.split(',')  # get list of all dependencies, separated with comma in string
        # Check number of dependencies / input fiepaths
        assert len(actual_dep) == len(cur_ref_node.input_filepaths)
        for ref_dep, cur_actual_dep in zip(cur_ref_node.input_filepaths, actual_dep):
            # Check input path match the correct dependency nodes
            assert cur_actual_dep.startswith(ref_dep)

    cleanup(out_filepath)


def test_airflow_dag_vrt_only(csw_server, test_folder, evi_file):
    
    setup_folder(test_folder)
    
    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-12346"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter(job_id, user_name, process_graph_json=evi_file, job_data=job_data, vrt_only=True)
    writer.write_and_move_job()

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'[A-Za-z]*_[A-Za-z0-9]* = ', out_content)[2:]  # Discard header and dag definition
    assert len(actual_nodes) == 14
    actual_nodes[13] = actual_nodes[13].split('\n\n')[0]

    for actual_node in actual_nodes:
        actual_params = actual_node.split('\n')[3].strip()
        actual_params = actual_params.split('=')[-1].strip()
        actual_params = eval(actual_params)
        for key, value in actual_params[-1].items():
            # Check output format is vrt
            if key == 'format_type':
                assert value == 'vrt'
            # TODO not in each cell?

    cleanup(out_filepath)


def test_airflow_dag_parallele(csw_server, test_folder, evi_file, ref_airflow_job_folder):    
    
    setup_folder(test_folder)
    
    job_data = os.path.join(test_folder, 'openeo_job')

    job_id = "jb-first_step"
    out_filepath = os.path.join(os.environ['AIRFLOW_DAGS'], 'dag_' + job_id + '.py')
    user_name = "jdoe_67890"

    writer = AirflowDagWriter(job_id, user_name, process_graph_json=evi_file, job_data=job_data, vrt_only=True)
    writer.write_and_move_job()
    
    # Simulate that job has ran (place vrt files in node folders)
    _, node_ids = writer.get_nodes()
    ref_node_ids = ['blue', 'dc', 'div', 'evi', 'min', 'mintime', 'nir', 'p1', 'p2', 'p3', 'red', 'save', 'sub', 'sum']
    for node_id in node_ids:
        node_folder = os.path.join(job_data, node_id)
        for ref_node_id in ref_node_ids:
            if ref_node_id == node_id.split('_')[0]:
                copytree(os.path.join(ref_airflow_job_folder, ref_node_id), node_folder)
    
    # (Re)write DAG, noe parallelised
    writer.parallelize_task = True
    writer.vrt_only = False
    writer.write_and_move_job()
    # TODO add checks
    
    rmtree(job_data)
    cleanup(out_filepath)
