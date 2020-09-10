import glob
from eodatareaders.eo_data_reader import EODataProcessor

### load_collection_0 ###
# node input files
filepaths = ['sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050118--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050118--_EU010M_E052N015T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050028--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050028--_EU010M_E052N016T1.tif', 'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N016T1.tif']
# node input pickled dc files
dc_filepaths = None

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/load_collection_0/'}, {'name': 'filter_bands', 'bands': ['VV', 'VH']}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/basic_job/load_collection_0/load_collection_0.dc;str'}]

# evaluate node
load_collection_0 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### mean_2 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/load_collection_0/load_collection_0.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/mean_2/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/basic_job/mean_2/mean_2.dc;str'}]

# evaluate node
mean_2 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### t_mean_1 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/mean_2/mean_2.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/t_mean_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/t_mean_1/t_mean_1.dc;str'}]

# evaluate node
t_mean_1 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### VH_5 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/t_mean_1/t_mean_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/VH_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'label': 'VH;str'}}, {'name': 'to_pickle', 'filepath': '/basic_job/VH_5/VH_5.dc;str'}]

# evaluate node
VH_5 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### VV_4 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/t_mean_1/t_mean_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/VV_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'label': 'VV;str'}}, {'name': 'to_pickle', 'filepath': '/basic_job/VV_4/VV_4.dc;str'}]

# evaluate node
VV_4 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### sub_6 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/VH_5/VH_5.dc', '/basic_job/VV_4/VV_4.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/sub_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/basic_job/sub_6/sub_6.dc;str'}]

# evaluate node
sub_6 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### cr_3 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/sub_6/sub_6.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/cr_3/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/cr_3/cr_3.dc;str'}]

# evaluate node
cr_3 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### add_dim_cr_7 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/cr_3/cr_3.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/add_dim_cr_7/'}, {'name': 'add_dimension', 'dim_name': 'band;str', 'label': 'B;str', 'dim_type': 'bands;str'}, {'name': 'to_pickle', 'filepath': '/basic_job/add_dim_cr_7/add_dim_cr_7.dc;str'}]

# evaluate node
add_dim_cr_7 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### VH_10 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/t_mean_1/t_mean_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/VH_10/'}, {'name': 'filter_bands', 'bands': ['VH']}, {'name': 'to_pickle', 'filepath': '/basic_job/VH_10/VH_10.dc;str'}]

# evaluate node
VH_10 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### rename_label_VH_11 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/VH_10/VH_10.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/rename_label_VH_11/'}, {'name': 'rename_labels', 'dim_name': 'band;str', 'new_labels': "['G'];list", 'old_labels': '[];list'}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/rename_label_VH_11/rename_label_VH_11.dc;str'}]

# evaluate node
rename_label_VH_11 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### VV_8 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/t_mean_1/t_mean_1.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/VV_8/'}, {'name': 'filter_bands', 'bands': ['VV']}, {'name': 'to_pickle', 'filepath': '/basic_job/VV_8/VV_8.dc;str'}]

# evaluate node
VV_8 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### rename_label_VV_9 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/VV_8/VV_8.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/rename_label_VV_9/'}, {'name': 'rename_labels', 'dim_name': 'band;str', 'new_labels': "['R'];list", 'old_labels': '[];list'}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/basic_job/rename_label_VV_9/rename_label_VV_9.dc;str'}]

# evaluate node
rename_label_VV_9 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### RG_12 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/rename_label_VV_9/rename_label_VV_9.dc', '/basic_job/rename_label_VH_11/rename_label_VH_11.dc']

# node input parameters
params = [{'name': 'set_output_folder', 'out_dirpath': '/basic_job/RG_12/'}, {'name': 'to_pickle', 'filepath': '/basic_job/RG_12/RG_12.dc;str'}]

# evaluate node
RG_12 = EODataProcessor(filepaths=filepaths, dc_filepaths=dc_filepaths, user_params=params)

### RGB_13 ###
# node input files
filepaths = None
# node input pickled dc files
dc_filepaths = ['/basic_job/RG_12/RG_12.dc', '/basic_job/add_dim_cr_7/add_dim_cr_7.dc']

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
