import glob
from eodatareaders.eo_data_reader import eoDataReader

### may_2 ###
# node input files
filepaths = ['/home/luca/eodc/data/copernicus.eu/s1b_csar_grdh_iw/2017/05/01/S1B_IW_GRDH_1SDV_20170501T050056_20170501T050121_005400_00976D_9BFC.zip', '/home/luca/eodc/data/copernicus.eu/s1b_csar_grdh_iw/2017/05/02/S1B_IW_GRDH_1SDV_20170502T165002_20170502T165027_005422_009812_283B.zip']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/may_2_0/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'quick_geocode', 'scale_sampling': '1;int'}, {'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/may_2/'}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}]

# evaluate node
may_2 = eoDataReader(filepaths, params)

### march_0 ###
# node input files
filepaths = ['/home/luca/eodc/data/copernicus.eu/s1a_csar_grdh_iw/2017/03/01/S1A_IW_GRDH_1SDV_20170301T050935_20170301T051000_015494_019728_3A01.zip', '/home/luca/eodc/data/copernicus.eu/s1b_csar_grdh_iw/2017/03/02/S1B_IW_GRDH_1SDV_20170302T050053_20170302T050118_004525_007E0D_CBC9.zip']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/march_0_0/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'quick_geocode', 'scale_sampling': '1;int'}, {'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/march_0/'}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}]

# evaluate node
march_0 = eoDataReader(filepaths, params)

### mean_4 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/march_0/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_4/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'eo_mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}]

# evaluate node
mean_4 = eoDataReader(filepaths, params)

### mean_march_3 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_4/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_march_3/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
mean_march_3 = eoDataReader(filepaths, params)

### R_band_9 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_march_3/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/R_band_9/'}, {'name': 'rename_labels', 'dimension': 'band', 'labels': ['R']}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}]

# evaluate node
R_band_9 = eoDataReader(filepaths, params)

### april_1 ###
# node input files
filepaths = ['/home/luca/eodc/data/copernicus.eu/s1a_csar_grdh_iw/2017/04/02/S1A_IW_GRDH_1SDV_20170402T165033_20170402T165058_015968_01A54C_7273.zip']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/april_1_0/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'quick_geocode', 'scale_sampling': '1;int'}, {'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/april_1/'}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}]

# evaluate node
april_1 = eoDataReader(filepaths, params)

### mean_6 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/april_1/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_6/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'eo_mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}]

# evaluate node
mean_6 = eoDataReader(filepaths, params)

### mean_april_5 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_6/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_april_5/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
mean_april_5 = eoDataReader(filepaths, params)

### G_band_10 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_april_5/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/G_band_10/'}, {'name': 'rename_labels', 'dimension': 'band', 'labels': ['G']}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}]

# evaluate node
G_band_10 = eoDataReader(filepaths, params)

### RG_12 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/R_band_9/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/G_band_10/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RG_12/'}, {'name': 'sort_cube'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
RG_12 = eoDataReader(filepaths, params)

### mean_8 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/may_2/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_8/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'eo_mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}]

# evaluate node
mean_8 = eoDataReader(filepaths, params)

### mean_may_7 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_8/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_may_7/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
mean_may_7 = eoDataReader(filepaths, params)

### B_band_11 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_may_7/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/B_band_11/'}, {'name': 'rename_labels', 'dimension': 'band', 'labels': ['B']}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}]

# evaluate node
B_band_11 = eoDataReader(filepaths, params)

### RGB_13 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RG_12/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/B_band_11/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RGB_13/'}, {'name': 'sort_cube'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
RGB_13 = eoDataReader(filepaths, params)

### save_result_14 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RGB_13/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/result/'}, {'name': 'create_composite', 'bands': ['R', 'G', 'B'], 'format_type': 'GTiff'}]

# evaluate node
save_result_14 = eoDataReader(filepaths, params)
