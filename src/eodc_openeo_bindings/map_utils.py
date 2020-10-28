"""

"""

from os import path
import inspect
import importlib
from numbers import Number
from eodc_openeo_bindings.map_cubes_processes import map_apply, map_reduce_dimension


def map_default(process, process_name, mapping, param_dict=None):
    """
    Maps all processes which have only data input and ignore_nodata option.
    """

    f_input = {}
    f_input['f_name'] = process_name

    if param_dict:
        parameters = get_process_params(process['arguments'], param_dict)
        for item in parameters:
            f_input[item] = parameters[item]

    process['f_input'] = f_input

    if mapping == 'apply':
        return map_apply(process)
    elif mapping == 'reduce':
        return map_reduce_dimension(process)


def get_process_params(process_args, param_dict):
    """
    Get parameters from a process, if they are in its definition.
    
    Arguments:
        process_args {dict} -- arguments sent by a process
                 {'argument_name': value}
            e.g. {'data': {'from_node': 'dc_0'}, 'index': 2}
        param_dict {dict} -- parameters needed by a process
                 {'parameter_name': 'parameter_type'}
            e.g. {'ignore_data': 'bool', 'p': 'int'}
    """

    process_params = {}
    for param in param_dict:
        if param in process_args:
            if param in ('y', 'mask') and isinstance(process_args[param], dict) and 'from_node' in process_args[param]:
                # Mapping for openeo processes which havs f(x, y) input rather than f(data)
                # NB this is used in eodatareaders/pixel_functions/geo_process
                process_params[param] = 'set' + param_dict[param] + ';str'
            elif isinstance(param_dict[param], list):
                # NOTE some python processes have different param names compared to the openEO process
                # see e.g. "clip"
                # https://github.com/Open-EO/openeo-processes-python/blob/master/src/openeo_processes/math.py
                # https://processes.openeo.org/#clip
                process_params[param_dict[param][0]] = str(process_args[param]) + ';' + param_dict[param][1]
            else:
                process_params[param] = str(process_args[param]) + ';' + param_dict[param]
        elif param == 'extra_values':
            # Needed in "sum" and "product"
            process_params[param] = param_dict[param]
    
    return process_params
    

def set_extra_values(process_args, add_extra_idxs=False):
    """
    
    """
    
    extra_values = []
    extra_idxs = []
    for k, item in enumerate(process_args['data']):
        if isinstance(item, Number):
            extra_values.append(item)
            if add_extra_idxs:
                extra_idxs.append(k)
    
    process_params = {}
    if extra_values:
        process_params['extra_values'] = str(extra_values) + ';list'
        if add_extra_idxs:
            process_params['extra_idxs'] = str(extra_idxs) + ';list'
    
    return process_params


def set_output_folder(root_folder, folder_name):
    """
    Appends folder to options.
    """

    # Set output_folder for this operation
    dict_item = {'name': 'set_output_folder',\
                 'out_dirpath': root_folder + path.sep + folder_name + path.sep}


    return [dict_item]
    

def get_mapped_processes():
    """
    Returns the openeo processes mapped and available on the back-end, sorted alphabetically.
    """
    
    modules = ['map_cubes_processes',
               'map_math_processes',
               'map_veg_indices_processes',
               'map_arrays_processes']
    
    processes = []
    for module_name in modules:
        module = importlib.import_module(module_name)
        funcs = inspect.getmembers(module, inspect.isfunction)
        for func in funcs:
            func_name = func[0]
            # func_callable = func[1] # just for clarity
            if func_name.startswith('map_'):
                processes.append(func_name.replace('map_', ''))
    
    return sorted(processes)
