"""

"""

from eodc_openeo_bindings.map_utils import map_default


def map_array_element(process):
    """
    
    """
    
    process_params = {'index': 'int', 'label': 'tr'}

    return map_default(process, 'eo_array_element', 'reduce', process_params)
