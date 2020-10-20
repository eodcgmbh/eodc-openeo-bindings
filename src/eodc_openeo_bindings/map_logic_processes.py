"""

"""

from eodc_openeo_bindings.map_utils import map_default


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

    return map_default(process, 'not_', 'reduce')


def map_if(process):
    """

    """

    return map_default(process, 'if_', 'reduce')


def map_any(process):
    """

    """

    return map_default(process, 'any_', 'reduce')


def map_all(process):
    """

    """

    return map_default(process, 'all_', 'reduce')
