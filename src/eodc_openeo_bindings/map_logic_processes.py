"""

"""

from eodc_openeo_bindings.map_utils import map_default, set_extra_values, get_process_params


def map_and(process):
    """

    """
    
    param_dict = {'y': 'bool'}

    return map_default(process, 'and_', 'reduce', param_dict)


def map_or(process):
    """

    """
    
    param_dict = {'y': 'bool'}

    return map_default(process, 'or_', 'reduce', param_dict)


def map_xor(process):
    """

    """
    
    param_dict = {'y': 'bool'}

    return map_default(process, 'xor_', 'reduce', param_dict)


def map_not(process):
    """

    """
    
    param_dict = {'y': 'bool'}

    return map_default(process, 'not_', 'apply', param_dict)


def map_if(process):
    """

    """

    param_dict = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})

    return map_default(process, 'if_', 'reduce', param_dict)


def map_any(process):
    """

    """

    process_params1 = set_extra_values(process['arguments'])
    process_params2 = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})
    
    return map_default(process, 'any_', 'reduce', {**process_params1, **process_params2})


def map_all(process):
    """

    """

    process_params1 = set_extra_values(process['arguments'])
    process_params2 = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})
    
    return map_default(process, 'all_', 'reduce', {**process_params1, **process_params2})
