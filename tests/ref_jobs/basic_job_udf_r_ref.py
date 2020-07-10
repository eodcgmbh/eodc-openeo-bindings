import glob
from eodatareaders.eo_data_reader import eoDataReader

### dc_0 ###
# node input files
filepaths = ['/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/output_udf_r/dc_0/'}, {'name': 'filter_bands', 'bands': [8]}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}]

# evaluate node
dc_0 = eoDataReader(filepaths, params)

### udf_2 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/output_udf_r/dc_0/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = {'udf': 'data2 = data*(-1); data2', 'runtime': 'R', 'output_folder': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/output_udf_r/udf_2'}

# evaluate node
udf_2 = UdfExec(filepaths, params)

### udfnode_1 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/output_udf_r/udf_2/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/output_udf_r/result/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
udfnode_1 = eoDataReader(filepaths, params)
