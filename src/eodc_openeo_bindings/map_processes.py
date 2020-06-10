"""
A module dostring.
"""

from eodc_openeo_bindings.map_cubes_processes import *
from eodc_openeo_bindings.map_math_processes import *
from eodc_openeo_bindings.map_veg_indices_processes import *
from eodc_openeo_bindings.map_array_processes import *
from eodc_openeo_bindings.map_utils import set_output_folder


def map_process(process, node_id, root_folder, 
                wrapper_name=None, wrapper_dimension=None,
                options=None, vrt_only=False):
    """
    Entry point.
    """
    
    # Match multiple names for load_collection (for backward compatibility)
    if process['process_id'] in ('get_data', 'get_collection'):
        process['process_id'] = 'load_collection'

    if not options:
        options = []

    filepaths = None

    # Add/set output folder
    set_output_folder(root_folder, node_id, options)            
    if wrapper_name:
        process['wrapper_name'] = wrapper_name
    if wrapper_dimension:
        process['wrapper_dimension'] = wrapper_dimension
        
    dict_items = eval("map_" + process['process_id'] + "(process)")
    
    if isinstance(dict_items, tuple):
        filepaths = dict_items[1]
        dict_items = dict_items[0]

    if not isinstance(dict_items, list):
        dict_items = [dict_items]
    
    if 'result' in process.keys() and process['result'] and process['process_id'] != 'save_result':
        # Add save_result node
        if vrt_only:
            dict_item = map_save_result(process, format_type='VRT')
        else:
            dict_item = map_save_result(process, format_type='Gtiff', in_place=True) 
        dict_items.extend(dict_item)
    elif process['process_id'] == 'save_result':
        if vrt_only:
            dict_items[0]['format_type'] = 'VRT'
    
    for dict_item in dict_items:
        options.append(dict_item)

    return options, filepaths
