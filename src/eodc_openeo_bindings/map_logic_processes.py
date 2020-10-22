"""

"""

from eodc_openeo_bindings.map_utils import map_default, set_extra_values, get_process_params


def map_and(process):
    """

    """

    return map_default(process, 'and_', 'reduce')


def map_or(process):
    """

    """

    return map_default(process, 'or_', 'reduce')


def map_xor(process):
    """

    """

    return map_default(process, 'xor_', 'reduce')


def map_not(process):
    """

    """

    return map_default(process, 'not_', 'apply')


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
