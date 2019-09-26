"""

"""

import os
import glob
from copy import deepcopy
from shutil import copyfile
from eodc_openeo_bindings.openeo_to_eodatareaders import openeo_to_eodatareaders


def write_airflow_dag(job_id, user_name, process_graph_json, job_data, user_email=None, job_description=None,
                      parallelize_tasks=False, vrt_only=False):
    """
    Creates an Apache Airflow DAG with eoDataReaders syntax from a parsed openEO process graph.
    """
    
    # Convert from openEO to eoDataReaders syntax
    nodes, graph = openeo_to_eodatareaders(process_graph_json, job_data)

    if not job_description:
        job_description = "No description provided."

    dag_filename = 'dag_' + job_id
    if parallelize_tasks:
        dag_filename += '_parallelize'
    dag_filename += '.py'
    
    dagfile = open(dag_filename, 'w+')

    # Add imports
    dagfile.write(
'''
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import eoDataReadersOp
'''
    )
    dagfile.write('\n')

    # Add default args
    dagfile.write(
'''
default_args = {{
    'owner': "{username}",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "{usermail}",
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': None,
    # 'catchup': False,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}}
'''.format(username=user_name, usermail=user_email)
    )

    # Add DAG instance
    dagfile.write(
'''
dag = DAG(dag_id="{dag_id}",
          description="{dag_description}",
          catchup=True,
          default_args=default_args)
'''.format(dag_id=job_id, dag_description=job_description)
    )
    
    # Add nodes
    node_parallel = {}
    dep_subnodes = {}
    for node in nodes:
        node_id = node[0]
        params = node[1]
        filepaths = node[2]
        node_dependencies = node[3]
        
        if parallelize_tasks:
            parallelizable, _, _ = check_params_key(params, 'per_file')
            node_parallel[node_id] = parallelizable
        else:
            parallelizable = False
            node_parallel[node_id] = False

        if (parallelize_tasks and parallelizable and not node_dependencies) or \
            (parallelize_tasks and parallelizable and filepaths):
            # Nodes without depedencies do not need parallelization
            # Nodes with filepaths are only coming from load_collection
            # NB raise proper error
            print("The following node has no dependency and was set to be parallelized: ", node_id)
            pass
        
        if node_dependencies:
            filepaths = get_input_paths(node_id, node_dependencies, job_data, parallelize=parallelize_tasks and parallelizable)
            if not filepaths:
                node_parallel[node_id] = False
        
        key_exists, value_matches, key_index = check_params_key(params, 'format_type', 'Gtiff')
        if key_exists and value_matches and vrt_only:
            params[key_index]['format_type'] = 'vrt'
        
        if parallelize_tasks and len(filepaths) > 1 and parallelizable:
            sub_nodes = []
            for k, filepath in enumerate(filepaths):
                node_sub_id = node_id + '_' + str(k+1)
                if isinstance(filepath, list):
                    quotes = ""
                else:
                    quotes = "'"
                dagfile_write_task(dagfile, node_sub_id, filepath, params, quotes=quotes)
                sub_nodes.append(node_id + '_' + str(k))
            dep_subnodes[node_id] = sub_nodes
        else:
            dagfile_write_task(dagfile, node_id, filepaths, params, quotes="")

    # Add node dependencies
    for node in nodes:
        node_id = node[0]
        params = node[1]
        filepaths = node[2]
        node_dependencies = node[3]
        if node_dependencies:
            node_dependencies2 = expand_node_dependencies(node_dependencies, dep_subnodes, node_parallel[node_id])
            for k, dep_list in enumerate(node_dependencies2):
                try:
                    if node_parallel[node_id]:
                        dagfile_write_dependencies(dagfile, dep_subnodes[node_id][k], dep_list)
                    else:
                        dagfile_write_dependencies(dagfile, node_id, dep_list)
                except:
                    import pdb; pdb.set_trace()


    # Close file
    dagfile.close()

    # Move file to DAGs folder (must copy/delete because of volumes mounted on different )
    copyfile(dag_filename, os.environ.get('AIRFLOW_DAGS') + "/" + dag_filename)
    os.remove(dag_filename)





#########################
## Auxiliary functions ##
#########################
    
def get_existing_node(job_folder, node_id):
    """
    Get matching node discarding the hash.
    """
    
    target_id = None
    if os.path.isdir(job_folder):
        subfolders = glob.glob(job_folder + '/*')
        for folder in subfolders:
            if node_id.split('_')[0] in folder.split('/')[-1]:
                target_id = folder
                
    return target_id


def check_params_key(params, key_name, key_value=None):
    
    key_name_exists = False
    value_name_matches = False
    
    for k, item in enumerate(params):
        if key_name in item.keys():
            key_name_exists = True
            if key_value and item[key_name] == key_value:
                value_name_matches = True
        index = k
        
    # double check that process is indeed parallelizable
    if key_name_exists:
        key_name_exists = check_f_input(params)
            
    return key_name_exists, value_name_matches, index
    
    
def check_f_input(params):
    
    not_parallelizable = (
        'filter_bands', 
        'filter_bbox', 
        'filter_temporal',
        'eo_array_element'
    )
    
    parallelizable = False
    for item in params:
        if 'f_input' in item.keys():
            if item['f_input']['f_name'] not in not_parallelizable:
                parallelizable = True
                
    return parallelizable
    


def dagfile_write_task(dagfile, id, filepaths, process_graph, quotes):
    """
    
    """        
    
    dagfile.write(
'''
{id} = eoDataReadersOp(task_id='{task_id}',
                        dag=dag,
                        input_filepaths={quotes}{filepaths}{quotes},
                        input_params={process_graph}
                        )
'''.format(id=id, task_id=id, filepaths=filepaths, process_graph=process_graph, quotes=quotes)
                    )
                    
def dagfile_write_dependencies(dagfile, node_id, dependencies):
    """
    
    """
    
    dagfile.write(
'''
{id}.set_upstream([{dependencies}])
'''.format(id=node_id, dependencies=",".join(map(str, dependencies)))
        )
                    

def get_input_paths(node_id, node_dependencies, job_data, parallelize):
    """
    Create filepaths as a list of folders or list of files
    """
    
    node_dependencies_path = []
    for dep in node_dependencies:
        dep_path = get_existing_node(job_data, dep)
        if not dep_path:
            dep_path = job_data + os.path.sep + node_id + os.path.sep   
        node_dependencies_path.append(dep_path)
    
    filepaths = []
    if parallelize:
        counter = 0
        while counter >= 0:
            counter += 1
            paths_tmp = []
            for k, _ in enumerate(node_dependencies_path):
                paths_tmp.extend(glob.glob(node_dependencies_path[k] + '/*_*_*_{value}_*'.format(value=str(counter))))
            if paths_tmp:
                filepaths.append(paths_tmp)
            else:
                counter = -1
    else:
        for item in node_dependencies_path:
            filepaths.extend(glob.glob(item + '/*'))
            
    return filepaths
    
    
def expand_node_dependencies(node_dependencies, dep_subnodes, split_dependencies=False):
    """
    Expand dependencies, in case a node had been split because of parallelize.
    """
        
    node_dependencies2 = []
    max_n = 1
    for dep in node_dependencies:
        if dep in dep_subnodes.keys():
            if split_dependencies:
                node_dependencies2.append(dep_subnodes[dep])
                max_n = max(max_n, len(dep_subnodes[dep]))
            else:
                node_dependencies2.extend(dep_subnodes[dep])
        else:
            if split_dependencies:
                node_dependencies2.append([dep])
            else:
                node_dependencies2.append(dep)
                        
    if split_dependencies:
        for k, dep in enumerate(node_dependencies2):
            if len(dep) < max_n and len(dep) > 1:
                print('somethign wrokńg here.')
            if len(dep) < max_n:
                node_dependencies2[k] = node_dependencies2[k] * max_n
        
        node_dependencies3 = []
        for k in range(max_n):
            tmp_deps = []
            for item in node_dependencies2:
                tmp_deps.append(item[k])
            node_dependencies3.append(tmp_deps)
    
    else:
        node_dependencies3 = [node_dependencies2]
            
    return node_dependencies3
