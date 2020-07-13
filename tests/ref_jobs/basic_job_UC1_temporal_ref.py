import glob
from eodatareaders.eo_data_reader import eoDataReader

### march_0 ###
# node input files
filepaths = ['/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050118--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050118--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050028--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050028--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N016T1.tif']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/march_0/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}]

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

### add_dim_R_9 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_march_3/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/add_dim_R_9/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
add_dim_R_9 = eoDataReader(filepaths, params)

### R_band_10 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/add_dim_R_9/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/R_band_10/'}, {'name': 'rename_labels', 'dimension': 'band', 'labels': ['R']}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}]

# evaluate node
R_band_10 = eoDataReader(filepaths, params)

### april_1 ###
# node input files
filepaths = ['/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHA_20170402_165033--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050126--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050151--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVA_20170402_165033--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050126--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050151--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHA_20170402_165033--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHA_20170402_165058--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050126--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050151--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVA_20170402_165033--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVA_20170402_165058--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050126--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050151--_EU010M_E052N016T1.tif']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/april_1/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}]

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

### add_dim_G_11 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_april_5/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/add_dim_G_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
add_dim_G_11 = eoDataReader(filepaths, params)

### G_band_12 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/add_dim_G_11/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/G_band_12/'}, {'name': 'rename_labels', 'dimension': 'band', 'labels': ['G']}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}]

# evaluate node
G_band_12 = eoDataReader(filepaths, params)

### RG_15 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/R_band_10/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/G_band_12/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RG_15/'}, {'name': 'sort_cube'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
RG_15 = eoDataReader(filepaths, params)

### may_2 ###
# node input files
filepaths = ['/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHA_20170502_164937--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHA_20170502_165002--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050056--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050121--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVA_20170502_164937--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVA_20170502_165002--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050056--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050121--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHA_20170502_165002--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050031--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050056--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVA_20170502_165002--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050031--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050056--_EU010M_E052N016T1.tif']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/may_2/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}]

# evaluate node
may_2 = eoDataReader(filepaths, params)

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

### add_dim_B_13 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/mean_may_7/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/add_dim_B_13/'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
add_dim_B_13 = eoDataReader(filepaths, params)

### B_band_14 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/add_dim_B_13/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/B_band_14/'}, {'name': 'rename_labels', 'dimension': 'band', 'labels': ['B']}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}]

# evaluate node
B_band_14 = eoDataReader(filepaths, params)

### RGB_16 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RG_15/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/B_band_14/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RGB_16/'}, {'name': 'sort_cube'}, {'name': 'save_raster', 'format_type': 'VRT'}]

# evaluate node
RGB_16 = eoDataReader(filepaths, params)

### save_result_17 ###
# node input files
input_filepaths = ['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/RGB_16/']
filepaths = []
for path in input_filepaths:
    filepaths.extend(sorted(glob.glob(path + '/*')))

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/basic_job/result/'}, {'name': 'create_composite', 'bands': ['R', 'G', 'B'], 'format_type': 'GTiff'}, {'name': 'get_cube_metadata'}]

# evaluate node
save_result_17 = eoDataReader(filepaths, params)
