"""
A module dostring.
"""

from eodc_openeo_bindings.map_cubes_processes import *
from eodc_openeo_bindings.map_math_processes import *
from eodc_openeo_bindings.map_veg_indices_processes import *
from eodc_openeo_bindings.map_array_processes import *
from eodc_openeo_bindings.map_utils import set_output_folder


def map_process(process, node_id, is_result, root_folder,
                wrapper_name=None, wrapper_dimension=None,
                vrt_only=False, last_node=False):
    """
    Map an openeo process to the eodatareaders syntax.
    """
    
    # Match multiple names for load_collection (for backward compatibility)
    if process['process_id'] in ('get_data', 'get_collection'):
        process['process_id'] = 'load_collection'

    # Add/set output folder
    if last_node:
        folder_name = 'result'
    else:
        folder_name = node_id
    job_params = set_output_folder(root_folder, folder_name)
    
    if wrapper_name:
        process['wrapper_name'] = wrapper_name
    if wrapper_dimension:
        process['wrapper_dimension'] = wrapper_dimension
    
    if process['process_id'] == 'merge_cubes':
        process['arguments']['cube2']['from_node'] = root_folder + '/' +  process['arguments']['cube2']['from_node'] + '/' + process['arguments']['cube2']['from_node'] + '.dc'
        
    process_params = eval("map_" + process['process_id'] + "(process)")
    
    if isinstance(process_params, tuple):
        # This should happen only for "load_collection"
        filepaths = process_params[1]
        process_params = process_params[0]
        
        if process['arguments']["id"][:2] in ('s1', 's3'):
            # Workaround to use S1 and S3 Level-1 data, which are not georeferenced
            # TODO for the moment this is a workaround (29.06.2020)
            job_params = set_output_folder(root_folder, node_id + '_0')
            # Add a 'quick_geocode' step before cropping/clipping
            process_params.insert(-1, {'name': 'quick_geocode', 'scale_sampling': '1;int'})
            process_params.insert(-1, set_output_folder(root_folder, node_id)[0])
    else:
        filepaths = None
    for param in process_params:
        job_params.append(param)
    
    # Check flags for saving output
    if is_result and process['process_id'] != 'save_result':
        # Add save_result node
        if vrt_only:
            process_params = map_save_result(process, format_type='VRT')
        else:
            process_params = map_save_result(process, format_type='Gtiff', in_place=True) 
        job_params.extend(process_params)
    elif process['process_id'] == 'save_result':
        if vrt_only:
            index = -1 # "save_result" is usually the last item in the list
            job_params[index]['format_type'] = 'VRT'
    
    if last_node:
        # Add call to save cube matadata as JSON
        job_params.append({'name': 'get_cube_metadata'})
        
    # Add step to create pickled datacube
    pickled_filepath = job_params[0]['out_dirpath'] + node_id + '.dc'
    job_params.append({'name': 'to_pickle', 'filepath': f'{pickled_filepath};str'})

    return job_params, filepaths
