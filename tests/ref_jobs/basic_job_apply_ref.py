import glob
from eodatareaders.eo_data_reader import EODataProcessor

### dc_0 ###
# node input files
filepaths = ['/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/'}, {'name': 'filter_bands', 'bands': [8, 4, 2]}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/dc_0.dc;str'}]

# evaluate node
dc_0 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mult_2 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/dc_0.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mult_2/'}, {'name': 'apply', 'f_input': {'f_name': 'multiply', 'y': '-1;float'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mult_2/mult_2.dc;str'}]

# evaluate node
mult_2 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### apply_multiply_1 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mult_2/mult_2.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/apply_multiply_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/apply_multiply_1/apply_multiply_1.dc;str'}]

# evaluate node
apply_multiply_1 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### save_3 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/apply_multiply_1/apply_multiply_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/result/save_3.dc;str'}]

# evaluate node
save_3 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)
