from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import eoDataReadersOp

default_args = {
    'owner': "jdoe_67890",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "None",
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(dag_id="jb-12345_parallelised",
          description="No description provided",
          catchup=True,
          max_active_runs=1,
          schedule_interval=None,
          default_args=default_args)

dc_0 = eoDataReadersOp(task_id='dc_0',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip', '/home/luca/eodc/data/copernicus.eu/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip', '/home/luca/eodc/data/copernicus.eu/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/'}, {'name': 'filter_bands', 'bands': ['B08', 'B04', 'B02']}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/dc_0.dc;str'}],
                        queue='process'
                        )

nir_2 = eoDataReadersOp(task_id='nir_2',
                        dag=dag,
                        input_filepaths=None,
                        input_dc_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/dc_0.dc'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '0;int'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/nir_2.dc;str'}],
                        queue='process'
                        )

red_3 = eoDataReadersOp(task_id='red_3',
                        dag=dag,
                        input_filepaths=None,
                        input_dc_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/dc_0.dc'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '1;int'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/red_3.dc;str'}],
                        queue='process'
                        )

blue_4 = eoDataReadersOp(task_id='blue_4',
                        dag=dag,
                        input_filepaths=None,
                        input_dc_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/dc_0.dc'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '2;int'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/blue_4.dc;str'}],
                        queue='process'
                        )

sub_5_1 = eoDataReadersOp(task_id='sub_5_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_035270a9d0cf_20180616T102019_20180616T102019_7_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_1c53babb87c6_20180613T101019_20180613T101019_6_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

sub_5_2 = eoDataReadersOp(task_id='sub_5_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_03643af8aa8e_20180613T101019_20180613T101019_6_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_363b6b0ec1cb_20180616T102019_20180616T102019_7_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

sub_5_3 = eoDataReadersOp(task_id='sub_5_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_496cc5cd9779_20180611T102021_20180611T102021_2_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_3d1e1d50a2ee_20180608T101021_20180608T101021_1_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

sub_5_4 = eoDataReadersOp(task_id='sub_5_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_523c56a4de6a_20180621T102021_20180621T102021_4_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_3dc5fbebbd63_20180611T102021_20180611T102021_2_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

sub_5_5 = eoDataReadersOp(task_id='sub_5_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_7c73c9895e00_20180608T101021_20180608T101021_1_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_98bd75c9088e_20180618T101021_20180618T101021_3_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

sub_5_6 = eoDataReadersOp(task_id='sub_5_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_a6738d234104_20180618T101021_20180618T101021_3_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_ec78f4613c4e_20180606T102019_20180606T102019_5_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

sub_5_7 = eoDataReadersOp(task_id='sub_5_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_b7ad0a7312af_20180606T102019_20180606T102019_5_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_f5dc7de8aa79_20180621T102021_20180621T102021_4_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/sub_5.dc;str'}],
                        queue='process'
                        )

p1_6_1 = eoDataReadersOp(task_id='p1_6_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_1c53babb87c6_20180613T101019_20180613T101019_6_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p1_6_2 = eoDataReadersOp(task_id='p1_6_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_363b6b0ec1cb_20180616T102019_20180616T102019_7_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p1_6_3 = eoDataReadersOp(task_id='p1_6_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_3d1e1d50a2ee_20180608T101021_20180608T101021_1_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p1_6_4 = eoDataReadersOp(task_id='p1_6_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_3dc5fbebbd63_20180611T102021_20180611T102021_2_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p1_6_5 = eoDataReadersOp(task_id='p1_6_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_98bd75c9088e_20180618T101021_20180618T101021_3_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p1_6_6 = eoDataReadersOp(task_id='p1_6_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_ec78f4613c4e_20180606T102019_20180606T102019_5_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p1_6_7 = eoDataReadersOp(task_id='p1_6_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00000_f5dc7de8aa79_20180621T102021_20180621T102021_4_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/p1_6.dc;str'}],
                        queue='process'
                        )

p2_7_1 = eoDataReadersOp(task_id='p2_7_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_16cbceddaa14_20180621T102021_20180621T102021_4_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

p2_7_2 = eoDataReadersOp(task_id='p2_7_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_181e7a50b679_20180613T101019_20180613T101019_6_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

p2_7_3 = eoDataReadersOp(task_id='p2_7_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_21a0f7cba20c_20180606T102019_20180606T102019_5_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

p2_7_4 = eoDataReadersOp(task_id='p2_7_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_255758d0dcb8_20180611T102021_20180611T102021_2_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

p2_7_5 = eoDataReadersOp(task_id='p2_7_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_2794d11ca08c_20180616T102019_20180616T102019_7_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

p2_7_6 = eoDataReadersOp(task_id='p2_7_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_2b3e5f9f89f7_20180608T101021_20180608T101021_1_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

p2_7_7 = eoDataReadersOp(task_id='p2_7_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00000_79307f8c18cb_20180618T101021_20180618T101021_3_arrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/p2_7.dc;str'}],
                        queue='process'
                        )

sum_8_1 = eoDataReadersOp(task_id='sum_8_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_035270a9d0cf_20180616T102019_20180616T102019_7_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_22b6f6d58b64_20180621T102021_20180621T102021_4_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_1bd3c0f6c1e6_20180621T102021_20180621T102021_4_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

sum_8_2 = eoDataReadersOp(task_id='sum_8_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_03643af8aa8e_20180613T101019_20180613T101019_6_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_3e95e97fc24c_20180608T101021_20180608T101021_1_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_532c57316eed_20180613T101019_20180613T101019_6_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

sum_8_3 = eoDataReadersOp(task_id='sum_8_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_496cc5cd9779_20180611T102021_20180611T102021_2_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_4ca0c207b34a_20180618T101021_20180618T101021_3_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_999048ffaa6c_20180606T102019_20180606T102019_5_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

sum_8_4 = eoDataReadersOp(task_id='sum_8_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_523c56a4de6a_20180621T102021_20180621T102021_4_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_5ba2dfbc691a_20180606T102019_20180606T102019_5_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_d0f6dfc15e93_20180608T101021_20180608T101021_1_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

sum_8_5 = eoDataReadersOp(task_id='sum_8_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_7c73c9895e00_20180608T101021_20180608T101021_1_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_5fc1ab649cad_20180611T102021_20180611T102021_2_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_ea413c394fb3_20180611T102021_20180611T102021_2_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

sum_8_6 = eoDataReadersOp(task_id='sum_8_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_a6738d234104_20180618T101021_20180618T101021_3_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_70debb07b030_20180613T101019_20180613T101019_6_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_ea6cb4ea4ed1_20180616T102019_20180616T102019_7_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

sum_8_7 = eoDataReadersOp(task_id='sum_8_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00000_b7ad0a7312af_20180606T102019_20180606T102019_5_arrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00000_a2f0363875a9_20180616T102019_20180616T102019_7_productarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00000_f3a91a002a71_20180618T101021_20180618T101021_3_productarrayelement.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/sum_8.dc;str'}],
                        queue='process'
                        )

div_9_1 = eoDataReadersOp(task_id='div_9_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_04ae61a7e121_20180606T102019_20180606T102019_5_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_15c6cc47f3f1_20180611T102021_20180611T102021_2_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

div_9_2 = eoDataReadersOp(task_id='div_9_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_2a4d9504ab87_20180618T101021_20180618T101021_3_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_2c5b9546a0ea_20180608T101021_20180608T101021_1_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

div_9_3 = eoDataReadersOp(task_id='div_9_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_59ad59b97ba9_20180608T101021_20180608T101021_1_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_2cf69366884d_20180606T102019_20180606T102019_5_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

div_9_4 = eoDataReadersOp(task_id='div_9_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_7aa8667bd393_20180621T102021_20180621T102021_4_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_5ed842fc9884_20180621T102021_20180621T102021_4_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

div_9_5 = eoDataReadersOp(task_id='div_9_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_84a103b35221_20180613T101019_20180613T101019_6_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_82dc6e872937_20180616T102019_20180616T102019_7_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

div_9_6 = eoDataReadersOp(task_id='div_9_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_88aec033b4cf_20180611T102021_20180611T102021_2_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_a517711a5dab_20180618T101021_20180618T101021_3_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

div_9_7 = eoDataReadersOp(task_id='div_9_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00000_98ba4098d264_20180616T102019_20180616T102019_7_subtractarrayelement.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00000_c589879978fc_20180613T101019_20180613T101019_6_sum.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/div_9.dc;str'}],
                        queue='process'
                        )

p3_10_1 = eoDataReadersOp(task_id='p3_10_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_3b19947b13bb_20180606T102019_20180606T102019_5_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

p3_10_2 = eoDataReadersOp(task_id='p3_10_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_3e23f7e4f34d_20180621T102021_20180621T102021_4_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

p3_10_3 = eoDataReadersOp(task_id='p3_10_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_524242e4a799_20180611T102021_20180611T102021_2_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

p3_10_4 = eoDataReadersOp(task_id='p3_10_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_5266d800c65a_20180618T101021_20180618T101021_3_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

p3_10_5 = eoDataReadersOp(task_id='p3_10_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_59951e825c67_20180608T101021_20180608T101021_1_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

p3_10_6 = eoDataReadersOp(task_id='p3_10_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_ca61bc817d47_20180616T102019_20180616T102019_7_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

p3_10_7 = eoDataReadersOp(task_id='p3_10_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00000_d3ad28b41ec6_20180613T101019_20180613T101019_6_divide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc;str'}],
                        queue='process'
                        )

evi_1 = eoDataReadersOp(task_id='evi_1',
                        dag=dag,
                        input_filepaths=None,
                        input_dc_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/p3_10.dc'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/evi_1.dc;str'}],
                        queue='process'
                        )

min_12_1 = eoDataReadersOp(task_id='min_12_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_477012afb166_20180613T101019_---------------_6_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

min_12_2 = eoDataReadersOp(task_id='min_12_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_5852cc369190_20180611T102021_---------------_2_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

min_12_3 = eoDataReadersOp(task_id='min_12_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_7445343dee29_20180616T102019_---------------_7_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

min_12_4 = eoDataReadersOp(task_id='min_12_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_771a9e3b2df9_20180608T101021_---------------_1_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

min_12_5 = eoDataReadersOp(task_id='min_12_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_a49e6871783c_20180606T102019_---------------_5_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

min_12_6 = eoDataReadersOp(task_id='min_12_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_b98051a06c4b_20180621T102021_---------------_4_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

min_12_7 = eoDataReadersOp(task_id='min_12_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00000_dd38c9eafbe1_20180618T101021_---------------_3_productdivide.vrt'],
                        input_dc_filepaths=None,
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc;str'}],
                        queue='process'
                        )

mintime_11 = eoDataReadersOp(task_id='mintime_11',
                        dag=dag,
                        input_filepaths=None,
                        input_dc_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/min_12.dc'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/mintime_11.dc;str'}],
                        queue='process'
                        )

save_13 = eoDataReadersOp(task_id='save_13',
                        dag=dag,
                        input_filepaths=None,
                        input_dc_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/mintime_11.dc'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/result/save_13.dc;str'}],
                        queue='process'
                        )

nir_2.set_upstream([dc_0])

red_3.set_upstream([dc_0])

blue_4.set_upstream([dc_0])

sub_5_1.set_upstream([nir_2,red_3])

sub_5_2.set_upstream([nir_2,red_3])

sub_5_3.set_upstream([nir_2,red_3])

sub_5_4.set_upstream([nir_2,red_3])

sub_5_5.set_upstream([nir_2,red_3])

sub_5_6.set_upstream([nir_2,red_3])

sub_5_7.set_upstream([nir_2,red_3])

p1_6_1.set_upstream([red_3])

p1_6_2.set_upstream([red_3])

p1_6_3.set_upstream([red_3])

p1_6_4.set_upstream([red_3])

p1_6_5.set_upstream([red_3])

p1_6_6.set_upstream([red_3])

p1_6_7.set_upstream([red_3])

p2_7_1.set_upstream([blue_4])

p2_7_2.set_upstream([blue_4])

p2_7_3.set_upstream([blue_4])

p2_7_4.set_upstream([blue_4])

p2_7_5.set_upstream([blue_4])

p2_7_6.set_upstream([blue_4])

p2_7_7.set_upstream([blue_4])

sum_8_1.set_upstream([nir_2,p1_6_1,p2_7_1])

sum_8_2.set_upstream([nir_2,p1_6_2,p2_7_2])

sum_8_3.set_upstream([nir_2,p1_6_3,p2_7_3])

sum_8_4.set_upstream([nir_2,p1_6_4,p2_7_4])

sum_8_5.set_upstream([nir_2,p1_6_5,p2_7_5])

sum_8_6.set_upstream([nir_2,p1_6_6,p2_7_6])

sum_8_7.set_upstream([nir_2,p1_6_7,p2_7_7])

div_9_1.set_upstream([sub_5_1,sum_8_1])

div_9_2.set_upstream([sub_5_2,sum_8_2])

div_9_3.set_upstream([sub_5_3,sum_8_3])

div_9_4.set_upstream([sub_5_4,sum_8_4])

div_9_5.set_upstream([sub_5_5,sum_8_5])

div_9_6.set_upstream([sub_5_6,sum_8_6])

div_9_7.set_upstream([sub_5_7,sum_8_7])

p3_10_1.set_upstream([div_9_1])

p3_10_2.set_upstream([div_9_2])

p3_10_3.set_upstream([div_9_3])

p3_10_4.set_upstream([div_9_4])

p3_10_5.set_upstream([div_9_5])

p3_10_6.set_upstream([div_9_6])

p3_10_7.set_upstream([div_9_7])

evi_1.set_upstream([p3_10_1,p3_10_2,p3_10_3,p3_10_4,p3_10_5,p3_10_6,p3_10_7])

min_12_1.set_upstream([evi_1])

min_12_2.set_upstream([evi_1])

min_12_3.set_upstream([evi_1])

min_12_4.set_upstream([evi_1])

min_12_5.set_upstream([evi_1])

min_12_6.set_upstream([evi_1])

min_12_7.set_upstream([evi_1])

mintime_11.set_upstream([min_12_1,min_12_2,min_12_3,min_12_4,min_12_5,min_12_6,min_12_7])

save_13.set_upstream([mintime_11])
