"""

"""

from eodc_openeo_bindings.map_utils import __map_default


def map_array_element(process):
    """
    
    """
    
    process_params = {}
    if 'index' in process['arguments']:
        process_params['index'] = str(process['arguments']['index']) + ';int'
    if 'label' in process['arguments']:
        process_params['label'] = str(process['arguments']['label']) + ';str'
    
    return __map_default(process, 'eo_array_element', 'reduce', **process_params)
