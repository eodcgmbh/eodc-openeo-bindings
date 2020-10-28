"""

"""

from eodc_openeo_bindings.map_utils import map_default, set_extra_values, get_process_params


def map_absolute(process):
    """
    
    """
    
    return map_default(process, 'absolute', 'apply')


def map_clip(process):
    """
    
    """
    
    param_dict = {'min': ['min_x', 'float'],
                  'max': ['max_x', 'float']}
    # NOTE some python processes have different param names compared to the openEO process
    # see e.g. "clip"
    # https://github.com/Open-EO/openeo-processes-python/blob/master/src/openeo_processes/math.py
    # https://processes.openeo.org/#clip
    
    return map_default(process, 'clip', 'apply', param_dict)


def map_divide(process):
    """
    
    """
    
    param_dict = {'y': 'float'}
    
    return map_default(process, 'divide', 'reduce', param_dict)
    
    
def map_linear_scale_range(process):
    """
    
    """
    
    param_dict = {'inputMin': ['input_min', 'float'], 'inputMax': ['input_max', 'float'],
                  'outputMin': ['output_min', 'float'], 'outputMax': ['output_max', 'float']}
    
    return map_default(process, 'linear_scale_range', 'apply', param_dict)
    
    
def map_max(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
        
    return map_default(process, 'max', 'reduce', param_dict)
    
    
def map_min(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'min', 'reduce', param_dict)
    
    
def map_mean(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'mean', 'reduce', param_dict)
    

def map_median(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'median', 'reduce', param_dict)
    
    
def map_mod(process):
    """
    
    """
    
    param_dict = {'y': 'float'}
    
    return map_default(process, 'mod', 'apply', param_dict)


def map_multiply(process):
    """
    
    """

    param_dict = {'y': 'float'}
    
    return map_default(process, 'multiply', 'apply', param_dict)
    
    
def map_power(process):
    """
    
    """
    
    param_dict = {'p': 'float'}
    
    return map_default(process, 'power', 'apply', param_dict)
    
    
def map_product(process):
    """
    openEO process "product" is an alias for "multiply".
    
    """

    process_params1 = set_extra_values(process['arguments'])
    process_params2 = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})
    
    return map_default(process, 'product', 'reduce', {**process_params1, **process_params2})
    
    
def map_quantiles(process):
    """
    
    """
    
    param_dict = {
        'probabilities': 'list', # list of float
        'q': 'int',
        'ignore_nodata': 'bool'
        }
    
    return map_default(process, 'quantiles', 'apply', param_dict)
    
    
def map_sd(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'sd', 'reduce', param_dict)
    
    
def map_sgn(process):
    """
    
    """
    
    return map_default(process, 'sgn', 'apply')
    
    
def map_sqrt(process):
    """
    
    """
    
    return map_default(process, 'sqrt', 'apply')
    
    
def map_subtract(process):
    """
    
    """
    
    param_dict = {'y': 'float'}
    
    return map_default(process, 'subtract', 'reduce', param_dict)
    
    
def map_sum(process):
    """
    
    """
    
    process_params1 = set_extra_values(process['arguments'])
    process_params2 = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})
        
    return map_default(process, 'sum', 'reduce', {**process_params1, **process_params2})    
    

def map_variance(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'variance', 'reduce', param_dict)
    
    
def map_e(process):
    """
    
    """
    
    return map_default(process, 'e', 'apply')
    
    
def map_pi(process):
    """
    
    """
    
    return map_default(process, 'pi', 'apply')
    
    
# def map_cummax(process):
#     """
# 
#     """
# 
#     # needs apply_dimension
# 
#     return map_default(process, 'cummax')
# 
# 
# def map_cumproduct(process):
#     """
# 
#     """
#     # needs apply_dimension
#     return map_default(process, 'cumproduct')
# 
# 
# def map_cumsum(process):
#     """
# 
#     """
#     # needs apply_dimension
#     return map_default(process, 'cummsum')
    
    
def map_exp(process):
    """
    
    """
    
    param_dict = {'p': 'float'}
    
    return map_default(process, 'exp', 'apply', param_dict)
    
    
def map_ln(process):
    """
    
    """
    
    return map_default(process, 'ln', 'apply')
    
    
def map_log(process):
    """
    
    """
    
    if 'base' in process['arguments'].keys():
        base = str(process['arguments']['ignore_nodata'])
    else:
        base = None
    
    process_params = {}
    process_params['base'] = ignore_nodata + ';float'
    
    return map_default(process, 'log', 'apply', process_params)
    
    
def map_ceil(process):
    """
    
    """
    
    return map_default(process, 'ceil', 'apply')
    
    
def map_floor(process):
    """
    
    """
    
    return map_default(process, 'floor', 'apply')
    
    
def map_int(process):
    """
    
    """
    
    return map_default(process, 'int', 'apply')
    
    
def map_round(process):
    """
    
    """
    
    param_dict = {'p': 'int'}
    
    return map_default(process, 'round', 'apply', process_params)
    

def map_arccos(process):
    """
    
    """
        
    return map_default(process, 'arccos', 'apply')
    
def map_arcosh(process):
    """
    
    """
        
    return map_default(process, 'arcosh', 'apply')
    

def map_arcsin(process):
    """
    
    """
        
    return map_default(process, 'arcsin', 'apply')
    

def map_arsinh(process):
    """
    
    """
        
    return map_default(process, 'arsinh', 'apply')
    
    
def map_arctan(process):
    """
    
    """
        
    return map_default(process, 'arctan', 'apply')
    
    
def map_arctan2(process):
    """
    
    """
        
    return map_default(process, 'arctan2', 'apply')
    
    
def map_artanh(process):
    """
    
    """
        
    return map_default(process, 'artanh', 'apply')
    
    
def map_cos(process):
    """
    
    """
        
    return map_default(process, 'cos', 'apply')
    

def map_cosh(process):
    """
    
    """
    
    return map_default(process, 'cosh', 'apply')
    
    
def map_sin(process):
    """
    
    """
    
    return map_default(process, 'sin', 'apply')
    
    
def map_sinh(process):
    """
    
    """
    
    return map_default(process, 'sinh', 'apply')
    

def map_tan(process):
    """
    
    """
    
    return map_default(process, 'tan', 'apply')
    
    
def map_tanh(process):
    """
    
    """
    
    return map_default(process, 'tanh', 'apply')
