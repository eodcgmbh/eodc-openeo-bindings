import glob
from eodatareaders.eo_data_reader import EODataProcessor

### dc_0 ###
# node input files
filepaths = ['/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip', '/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip', '/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip', '/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip', '/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip', '/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/dc_0/'}, {'name': 'filter_bands', 'bands': ['B08', 'B04', 'B02']}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': './basic_job/dc_0/dc_0.dc;str'}]

# evaluate node
dc_0 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### blue_4 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/dc_0/dc_0.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/blue_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '2;int'}}, {'name': 'to_pickle', 'filepath': './basic_job/blue_4/blue_4.dc;str'}]

# evaluate node
blue_4 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### p2_7 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/blue_4/blue_4.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': './basic_job/p2_7/p2_7.dc;str'}]

# evaluate node
p2_7 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### red_3 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/dc_0/dc_0.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/red_3/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '1;int'}}, {'name': 'to_pickle', 'filepath': './basic_job/red_3/red_3.dc;str'}]

# evaluate node
red_3 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### p1_6 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/red_3/red_3.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': './basic_job/p1_6/p1_6.dc;str'}]

# evaluate node
p1_6 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### nir_2 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/dc_0/dc_0.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/nir_2/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '0;int'}}, {'name': 'to_pickle', 'filepath': './basic_job/nir_2/nir_2.dc;str'}]

# evaluate node
nir_2 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### sum_8 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/nir_2/nir_2.dc', './basic_job/p1_6/p1_6.dc', './basic_job/p2_7/p2_7.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': './basic_job/sum_8/sum_8.dc;str'}]

# evaluate node
sum_8 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### sub_5 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/nir_2/nir_2.dc', './basic_job/red_3/red_3.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': './basic_job/sub_5/sub_5.dc;str'}]

# evaluate node
sub_5 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### div_9 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/sub_5/sub_5.dc', './basic_job/sum_8/sum_8.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': './basic_job/div_9/div_9.dc;str'}]

# evaluate node
div_9 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### p3_10 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/div_9/div_9.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': './basic_job/p3_10/p3_10.dc;str'}]

# evaluate node
p3_10 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### evi_1 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/p3_10/p3_10.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/evi_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': './basic_job/evi_1/evi_1.dc;str'}]

# evaluate node
evi_1 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### min_12 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/evi_1/evi_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': './basic_job/min_12/min_12.dc;str'}]

# evaluate node
min_12 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mintime_11 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/min_12/min_12.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/mintime_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': './basic_job/mintime_11/mintime_11.dc;str'}]

# evaluate node
mintime_11 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### save_13 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./basic_job/mintime_11/mintime_11.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './basic_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': './basic_job/result/save_13.dc;str'}]

# evaluate node
save_13 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)
