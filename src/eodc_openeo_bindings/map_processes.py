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
                vrt_only=False):
    """
    Entry point.
    """
    
    # Match multiple names for load_collection (for backward compatibility)
    if process['process_id'] in ('get_data', 'get_collection'):
        process['process_id'] = 'load_collection'

    # Add/set output folder
    job_params = set_output_folder(root_folder, node_id)
    
    if wrapper_name:
        process['wrapper_name'] = wrapper_name
    if wrapper_dimension:
        process['wrapper_dimension'] = wrapper_dimension
        
    process_params = eval("map_" + process['process_id'] + "(process)")
    
    if isinstance(process_params, tuple):
        # This should happen only for "load_collection"
        filepaths = process_params[1]
        process_params = process_params[0]
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

    return job_params, filepaths
