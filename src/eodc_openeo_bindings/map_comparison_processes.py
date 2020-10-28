"""

"""

from eodc_openeo_bindings.map_utils import map_default


def map_lt(process):
    """

    """

    param_dict = {'y': 'float'}

    return map_default(process, 'lt', 'apply', param_dict)


def map_lte(process):
    """

    """

    param_dict = {'y': 'float'}

    return map_default(process, 'lte', 'apply', param_dict)


def map_gt(process):
    """

    """

    param_dict = {'y': 'float'}

    return map_default(process, 'gt', 'apply', param_dict)


def map_gte(process):
    """

    """

    param_dict = {'y': 'float'}

    return map_default(process, 'gte', 'apply', param_dict)


def map_eq(process):
    """

    """

    param_dict = {'y': 'numpy.array'}
    # NOTE: how to map type dynamically to support strings?
    if 'delta' in process['arguments']:
        param_dict['delta'] = 'int'
    if 'case_sensitive' in process['arguments']:
        param_dict['case_sensitive'] = 'bool'

    return map_default(process, 'eq', 'apply', param_dict)
