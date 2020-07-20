import glob
from eodatareaders.eo_data_reader import eoDataReader

### dc_0 ###
# node input files
filepaths = ['/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/'}, {'name': 'filter_bands', 'bands': [8, 4, 2]}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}]

# evaluate node
dc_0 = eoDataReader(filepaths, params)

### blue_4 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/blue_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '2;int'}}]

# evaluate node
blue_4 = eoDataReader(filepaths, params)

### p2_7 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/blue_4/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}]

# evaluate node
p2_7 = eoDataReader(filepaths, params)

### red_3 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/red_3/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '1;int'}}]

# evaluate node
red_3 = eoDataReader(filepaths, params)

### p1_6 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/red_3/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}]

# evaluate node
p1_6 = eoDataReader(filepaths, params)

### nir_2 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/dc_0/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/nir_2/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '0;int'}}]

# evaluate node
nir_2 = eoDataReader(filepaths, params)

### sum_8 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/nir_2/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/p1_6/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/p2_7/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}]

# evaluate node
sum_8 = eoDataReader(filepaths, params)

### sub_5 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/nir_2/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/red_3/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}]

# evaluate node
sub_5 = eoDataReader(filepaths, params)

### div_9 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/sub_5/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/sum_8/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}]

# evaluate node
div_9 = eoDataReader(filepaths, params)

### p3_10 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/div_9/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}]

# evaluate node
p3_10 = eoDataReader(filepaths, params)

### evi_1 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/p3_10/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/evi_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
evi_1 = eoDataReader(filepaths, params)

### min_12 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/evi_1/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}]

# evaluate node
min_12 = eoDataReader(filepaths, params)

### mintime_11 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/min_12/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mintime_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
mintime_11 = eoDataReader(filepaths, params)

### save_13 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mintime_11/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}]

# evaluate node
save_13 = eoDataReader(filepaths, params)
