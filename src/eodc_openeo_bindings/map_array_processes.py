"""

"""

from eodc_openeo_bindings.map_utils import map_default


def map_array_element(process):
    """
    
    """
    
    if 'label' in process['arguments'] and 'index' in process['arguments']:
        # TODO raise openEO error: ArrayElementParameterConflict
        msg = "Only one parameter between 'label' and 'index' may be specified. See https://processes.openeo.org/#array_element."
        raise(msg)
    if not 'label' in process['arguments'] and not 'index' in process['arguments']:
        # ODO raise openEO error: ArrayElementParameterMissing
        msg = "One parameter between 'label' and 'index' must be specified. See https://processes.openeo.org/#array_element."
        raise(msg)
    
    process_params = {}
    if 'index' in process['arguments']:
        process_params['index'] = 'int'
    elif 'label' in process['arguments']:
        if isinstance(process['arguments']['label'], int):
            process_params['label'] = 'int'
        elif isinstance(process['arguments']['label'], str):
            process_params['label'] = 'str'
    process_params['return_nodata'] = 'bool'

    return map_default(process, 'array_element', 'reduce', process_params)


def map_mask(process):
    """

    """

    param_dict = {
        'mask': 'int',
        'replacement': 'float'
    }

    return map_default(process, 'mask', 'reduce', param_dict)
