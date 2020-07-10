"""

"""

from eodc_openeo_bindings.map_utils import map_default, set_extra_values, get_process_params


def map_absolute(process):
    """
    
    """
    
    return map_default(process, 'eo_clip', 'apply')


def map_clip(process):
    """
    
    """
    
    param_dict = {'min': 'float', 'max': 'float'}
    
    return map_default(process, 'eo_clip', 'apply', param_dict)


def map_divide(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_divide', 'reduce', param_dict)
    
    
def map_linear_scale_range(process):
    """
    
    """
    
    param_dict = {'input_min': 'float', 'input_max': 'float',
                  'output_min': 'float', 'output_max': 'float'}
    
    return map_default(process, 'eo_linear_scale_range', 'apply', param_dict)
    
    
def map_max(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
        
    return map_default(process, 'eo_max', 'reduce', param_dict)
    
    
def map_min(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_min', 'reduce', param_dict)
    
    
def map_mean(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_mean', 'reduce', param_dict)
    

def map_median(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_median', 'reduce', param_dict)
    
    
def map_mod(process):
    """
    
    """
    
    param_dict = {'y': 'float'}
    
    return map_default(process, 'eo_mod', 'apply', param_dict)


def map_multiply(process):
    """
    
    """

    param_dict = {'y': 'float'}
    
    return map_default(process, 'eo_multiply', 'apply', param_dict)
    
    
def map_power(process):
    """
    
    """
    
    param_dict = {'p': 'float'}
    
    return map_default(process, 'eo_power', 'apply', param_dict)
    
    
def map_product(process):
    """
    openEO process "product" is an alias for "multiply".
    
    """

    process_params1 = set_extra_values(process['arguments'])
    process_params2 = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})
    
    return map_default(process, 'eo_product', 'reduce', {**process_params1, **process_params2})
    
    
def map_quantiles(process):
    """
    
    """
    
    param_dict = {
        'probabilities': 'list', # list of float
        'q': 'int',
        'ignore_nodata': 'bool'
        }
    
    return map_default(process, 'eo_quantiles', 'apply', param_dict)
    
    
def map_sd(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_sd', 'reduce', param_dict)
    
    
def map_sgn(process):
    """
    
    """
    
    return map_default(process, 'eo_sgn', 'apply')
    
    
def map_sqrt(process):
    """
    
    """
    
    return map_default(process, 'eo_sqrt', 'apply')
    
    
def map_subtract(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_subtract', 'reduce', param_dict)
    
    
def map_sum(process):
    """
    
    """
    
    process_params1 = set_extra_values(process['arguments'])
    process_params2 = get_process_params(process['arguments'], {'ignore_nodata': 'bool'})
        
    return map_default(process, 'eo_sum', 'reduce', {**process_params1, **process_params2})    
    

def map_variance(process):
    """
    
    """
    
    param_dict = {'ignore_nodata': 'bool'}
    
    return map_default(process, 'eo_variance', 'reduce', param_dict)
    
    
def map_e(process):
    """
    
    """
    
    return map_default(process, 'eo_e', 'apply')
    
    
def map_pi(process):
    """
    
    """
    
    return map_default(process, 'eo_pi', 'apply')
    
    
# def map_cummax(process):
#     """
# 
#     """
# 
#     # needs apply_dimension
# 
#     return map_default(process, 'eo_cummax')
# 
# 
# def map_cumproduct(process):
#     """
# 
#     """
#     # needs apply_dimension
#     return map_default(process, 'eo_cumproduct')
# 
# 
# def map_cumsum(process):
#     """
# 
#     """
#     # needs apply_dimension
#     return map_default(process, 'eo_cummsum')
    
    
def map_exp(process):
    """
    
    """
    
    param_dict = {'p': 'float'}
    
    return map_default(process, 'eo_exp', 'apply', param_dict)
    
    
def map_ln(process):
    """
    
    """
    
    return map_default(process, 'eo_ln', 'apply')
    
    
def map_log(process):
    """
    
    """
    
    if 'base' in process['arguments'].keys():
        base = str(process['arguments']['ignore_nodata'])
    else:
        base = None
    
    process_params = {}
    process_params['base'] = ignore_nodata + ';float'
    
    return map_default(process, 'eo_log', 'apply', process_params)
    
    
def map_ceil(process):
    """
    
    """
    
    return map_default(process, 'eo_ceil', 'apply')
    
    
def map_floor(process):
    """
    
    """
    
    return map_default(process, 'eo_floor', 'apply')
    
    
def map_int(process):
    """
    
    """
    
    return map_default(process, 'eo_int', 'apply')
    
    
def map_round(process):
    """
    
    """
    
    param_dict = {'p': 'int'}
    
    return map_default(process, 'eo_round', 'apply', process_params)
    

def map_arccos(process):
    """
    
    """
        
    return map_default(process, 'eo_arccos', 'apply')
    
def map_arcosh(process):
    """
    
    """
        
    return map_default(process, 'eo_arcosh', 'apply')
    

def map_arcsin(process):
    """
    
    """
        
    return map_default(process, 'eo_arcsin', 'apply')
    

def map_arsinh(process):
    """
    
    """
        
    return map_default(process, 'eo_arsinh', 'apply')
    
    
def map_arctan(process):
    """
    
    """
        
    return map_default(process, 'eo_arctan', 'apply')
    
    
def map_arctan2(process):
    """
    
    """
        
    return map_default(process, 'eo_arctan2', 'apply')
    
    
def map_artanh(process):
    """
    
    """
        
    return map_default(process, 'eo_artanh', 'apply')
    
    
def map_cos(process):
    """
    
    """
        
    return map_default(process, 'eo_cos', 'apply')
    

def map_cosh(process):
    """
    
    """
    
    return map_default(process, 'eo_cosh', 'apply')
    
    
def map_sin(process):
    """
    
    """
    
    return map_default(process, 'eo_sin', 'apply')
    
    
def map_sinh(process):
    """
    
    """
    
    return map_default(process, 'eo_sinh', 'apply')
    

def map_tan(process):
    """
    
    """
    
    return map_default(process, 'eo_tan', 'apply')
    
    
def map_tanh(process):
    """
    
    """
    
    return map_default(process, 'eo_tanh', 'apply')
