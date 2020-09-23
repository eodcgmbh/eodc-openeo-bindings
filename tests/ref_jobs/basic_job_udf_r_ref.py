import glob
from eodatareaders.eo_data_reader import EODataProcessor

### dc_0 ###
# node input files
filepaths = ['/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './output_udf_r/dc_0/'}, {'name': 'filter_bands', 'bands': [8]}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': './output_udf_r/dc_0/dc_0.dc;str'}]

# evaluate node
dc_0 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### udf_2 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./output_udf_r/dc_0/dc_0.dc']

# node input parameters
params = {'udf': 'data2 = data*(-1); data2', 'runtime': 'R', 'output_folder': './output_udf_r/udf_2'}

# evaluate node
udf_2 = UdfExec(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### udfnode_1 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['./output_udf_r/udf_2/udf_2.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': './output_udf_r/result/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': './output_udf_r/result/udfnode_1.dc;str'}]

# evaluate node
udfnode_1 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)
