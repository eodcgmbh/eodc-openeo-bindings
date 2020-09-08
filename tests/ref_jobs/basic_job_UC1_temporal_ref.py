import glob
from eodatareaders.eo_data_reader import EODataProcessor

### march_0 ###
# node input files
filepaths = ['/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050118--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050118--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050028--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050028--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N016T1.tif']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/march_0/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/basic_job/march_0/march_0.dc;str'}]

# evaluate node
march_0 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_4 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/march_0/march_0.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_4/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_4/mean_4.dc;str'}]

# evaluate node
mean_4 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_march_3 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_4/mean_4.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_march_3/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_march_3/mean_march_3.dc;str'}]

# evaluate node
mean_march_3 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### add_dim_R_9 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_march_3/mean_march_3.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/add_dim_R_9/'}, {'name': 'add_dimension', 'dim_name': 'band;str', 'label': 'R;str', 'dim_type': 'bands;str'}, {'name': 'to_pickle', 'filepath': '/basic_job/add_dim_R_9/add_dim_R_9.dc;str'}]

# evaluate node
add_dim_R_9 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### may_2 ###
# node input files
filepaths = ['/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHA_20170502_164937--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHA_20170502_165002--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050056--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050121--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVA_20170502_164937--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVA_20170502_165002--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050056--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050121--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHA_20170502_165002--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050031--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170501_050056--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVA_20170502_165002--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050031--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170501_050056--_EU010M_E052N016T1.tif']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/may_2/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/basic_job/may_2/may_2.dc;str'}]

# evaluate node
may_2 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_8 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/may_2/may_2.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_8/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_8/mean_8.dc;str'}]

# evaluate node
mean_8 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_may_7 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_8/mean_8.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_may_7/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_may_7/mean_may_7.dc;str'}]

# evaluate node
mean_may_7 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### add_dim_B_11 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_may_7/mean_may_7.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/add_dim_B_11/'}, {'name': 'add_dimension', 'dim_name': 'band;str', 'label': 'B;str', 'dim_type': 'bands;str'}, {'name': 'to_pickle', 'filepath': '/basic_job/add_dim_B_11/add_dim_B_11.dc;str'}]

# evaluate node
add_dim_B_11 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### april_1 ###
# node input files
filepaths = ['/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHA_20170402_165033--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050126--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050151--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVA_20170402_165033--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050126--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050151--_EU010M_E052N015T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHA_20170402_165033--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHA_20170402_165058--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050126--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170401_050151--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVA_20170402_165033--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVA_20170402_165058--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050126--_EU010M_E052N016T1.tif', '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170401_050151--_EU010M_E052N016T1.tif']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/april_1/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/basic_job/april_1/april_1.dc;str'}]

# evaluate node
april_1 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_6 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/april_1/april_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_6/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_6/mean_6.dc;str'}]

# evaluate node
mean_6 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_april_5 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_6/mean_6.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_april_5/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_april_5/mean_april_5.dc;str'}]

# evaluate node
mean_april_5 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### add_dim_G_10 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_april_5/mean_april_5.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/add_dim_G_10/'}, {'name': 'add_dimension', 'dim_name': 'band;str', 'label': 'G;str', 'dim_type': 'bands;str'}, {'name': 'to_pickle', 'filepath': '/basic_job/add_dim_G_10/add_dim_G_10.dc;str'}]

# evaluate node
add_dim_G_10 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### RG_12 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/add_dim_R_9/add_dim_R_9.dc', '/basic_job/add_dim_G_10/add_dim_G_10.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/RG_12/'}, {'name': 'to_pickle', 'filepath': '/basic_job/RG_12/RG_12.dc;str'}]

# evaluate node
RG_12 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### RGB_13 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/RG_12/RG_12.dc', '/basic_job/add_dim_B_11/add_dim_B_11.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/RGB_13/'}, {'name': 'to_pickle', 'filepath': '/basic_job/RGB_13/RGB_13.dc;str'}]

# evaluate node
RGB_13 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### save_result_14 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/RGB_13/RGB_13.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/result/'}, {'name': 'create_composite', 'bands': ['R', 'G', 'B'], 'format_type': 'GTiff'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': '/basic_job/result/save_result_14.dc;str'}]

# evaluate node
save_result_14 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)
