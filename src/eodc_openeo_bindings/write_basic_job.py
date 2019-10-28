"""

"""

import os
import nbformat as nbf
from eodc_openeo_bindings.openeo_to_eodatareaders import openeo_to_eodatareaders


def write_basic_job(process_graph_json, job_data, python_filepath=None):
    """
    
    """
    
    if not python_filepath:
        python_filepath = 'test.py'
    basic_job = open(python_filepath, 'w+')    

    # Convert from openEO to eoDataReaders syntax
    nodes, graph = openeo_to_eodatareaders(process_graph_json, job_data)
        
    # Add imports
    basic_job.write(
'''\
import glob
from eodatareaders.eo_data_reader import eoDataReader
'''
    )
    basic_job.write('\n')

    translated_nodes = {}
    translated_nodes_keys = []
    for node in nodes:
        node_id = node[0]
        params = node[1]
        filepaths = node[2]
        node_dependencies = node[3]
        
        if filepaths:
            filepaths0 = 'filepaths = '
        else:
            if not node_dependencies:
                error("No filepaths and no node dependencies for node:{node_id}".format(node_id=node_id))
            
            filepaths0 = ''
            filepaths = []
            for dep in node_dependencies:
                filepaths.append(job_data + os.path.sep + dep + os.path.sep)
            filepaths = get_file_list(filepaths)
            

        translated_nodes[node_id] = '''\
### {node_id} ###
# node input files
{filepaths0}{filepaths}

# node input parameters
params = {params}

# evaluate node
{node_id} = eoDataReader(filepaths, params)

'''.format(node_id=node_id, params=params, filepaths=filepaths, filepaths0=filepaths0)
                
        translated_nodes_keys.append(node_id)
    
    for node in nodes:
        node_id = node[0]
        params = node[1]
        filepaths = node[2]
        node_dependencies = node[3]
        
        current_index = translated_nodes_keys.index(node_id)
        dep_indices = []
        if node_dependencies:
            for dep in node_dependencies:
                dep_indices.append(translated_nodes_keys.index(dep)) 
        else:
            dep_indices.append(0)
        
        this_node = translated_nodes_keys.pop(current_index)
        translated_nodes_keys.insert(max(dep_indices) + 1, this_node)
    
    # Write to jupyter notebook in correct order
    for node_id in translated_nodes_keys:
        basic_job.write(translated_nodes[node_id])
    
    # Close file
    basic_job.close()
        
        
def get_file_list(filepaths):
    """
    
    """
            
    if isinstance(filepaths, str):
        
        file_list = """\
filepaths = sorted(glob.glob('{input_filepaths}' + '/*'))""".format(input_filepaths=filepaths)

    elif isinstance(filepaths, list):
        file_list = """\
input_filepaths = {input_filepaths}
filepaths = []
for path in {input_filepaths}:
    filepaths.extend(sorted(glob.glob(path + '/*')))""".format(input_filepaths=filepaths)
    
    return file_list
    
