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
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/'}, {'name': 'filter_bands', 'bands': [8, 4, 2]}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}],
                        queue='process'
                        )

nir_2 = eoDataReadersOp(task_id='nir_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00011-532f9516_20180618T101021_---------------_3_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00004-b47ce805_20180621T102021_---------------_4_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00005-e1c20a57_20180608T101021_---------------_1_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00012-73d9c3a7_20180621T102021_---------------_4_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00009-8379b744_20180608T101021_---------------_1_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00002-30d35e12_20180611T102021_---------------_2_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00010-b9af6a6c_20180611T102021_---------------_2_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00007-b45742b8_20180618T101021_---------------_3_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00001-f8b0adb9_20180608T101021_---------------_1_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00008-57d5851d_20180621T102021_---------------_4_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00003-74675513_20180618T101021_---------------_3_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00006-f4f264f4_20180611T102021_---------------_2_4.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_array_element', 'index': '0;int'}}],
                        queue='process'
                        )

red_3 = eoDataReadersOp(task_id='red_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00011-532f9516_20180618T101021_---------------_3_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00004-b47ce805_20180621T102021_---------------_4_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00005-e1c20a57_20180608T101021_---------------_1_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00012-73d9c3a7_20180621T102021_---------------_4_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00009-8379b744_20180608T101021_---------------_1_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00002-30d35e12_20180611T102021_---------------_2_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00010-b9af6a6c_20180611T102021_---------------_2_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00007-b45742b8_20180618T101021_---------------_3_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00001-f8b0adb9_20180608T101021_---------------_1_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00008-57d5851d_20180621T102021_---------------_4_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00003-74675513_20180618T101021_---------------_3_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00006-f4f264f4_20180611T102021_---------------_2_4.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_array_element', 'index': '1;int'}}],
                        queue='process'
                        )

blue_4 = eoDataReadersOp(task_id='blue_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00011-532f9516_20180618T101021_---------------_3_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00004-b47ce805_20180621T102021_---------------_4_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00005-e1c20a57_20180608T101021_---------------_1_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00012-73d9c3a7_20180621T102021_---------------_4_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00009-8379b744_20180608T101021_---------------_1_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00002-30d35e12_20180611T102021_---------------_2_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00010-b9af6a6c_20180611T102021_---------------_2_2.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00007-b45742b8_20180618T101021_---------------_3_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00001-f8b0adb9_20180608T101021_---------------_1_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00008-57d5851d_20180621T102021_---------------_4_4.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00003-74675513_20180618T101021_---------------_3_8.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/00006-f4f264f4_20180611T102021_---------------_2_4.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_array_element', 'index': '2;int'}}],
                        queue='process'
                        )

sub_5_1 = eoDataReadersOp(task_id='sub_5_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00001-6b931b6e_20180608T101021_20180608T101021_1_eo-array-element-f07f78.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00001-cd9b5531_20180608T101021_20180608T101021_1_eo-array-element-831dab.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_subtract'}}],
                        queue='process'
                        )

sub_5_2 = eoDataReadersOp(task_id='sub_5_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00002-f108a3a9_20180611T102021_20180611T102021_2_eo-array-element-ff8efa.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00002-22e93bda_20180611T102021_20180611T102021_2_eo-array-element-640441.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_subtract'}}],
                        queue='process'
                        )

sub_5_3 = eoDataReadersOp(task_id='sub_5_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00003-6c2f0ae7_20180618T101021_20180618T101021_3_eo-array-element-a9a46d.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00003-fd285fdd_20180618T101021_20180618T101021_3_eo-array-element-ab036b.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_subtract'}}],
                        queue='process'
                        )

sub_5_4 = eoDataReadersOp(task_id='sub_5_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00004-1d2e6450_20180621T102021_20180621T102021_4_eo-array-element-ea054d.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00004-2c7a6ed6_20180621T102021_20180621T102021_4_eo-array-element-a648f1.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_subtract'}}],
                        queue='process'
                        )

p1_6 = eoDataReadersOp(task_id='p1_6',
                        dag=dag,
                        input_filepaths=[['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00001-cd9b5531_20180608T101021_20180608T101021_1_eo-array-element-831dab.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00002-22e93bda_20180611T102021_20180611T102021_2_eo-array-element-640441.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00003-fd285fdd_20180618T101021_20180618T101021_3_eo-array-element-ab036b.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/00004-2c7a6ed6_20180621T102021_20180621T102021_4_eo-array-element-a648f1.vrt']],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_product', 'extra_values': '[6];list'}}],
                        queue='process'
                        )

p2_7 = eoDataReadersOp(task_id='p2_7',
                        dag=dag,
                        input_filepaths=[['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00001-9befffaa_20180608T101021_20180608T101021_1_eo-array-element-3aacb5.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00002-ec0c7512_20180611T102021_20180611T102021_2_eo-array-element-d21309.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00003-5937e517_20180618T101021_20180618T101021_3_eo-array-element-c2677f.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/00004-a2803c08_20180621T102021_20180621T102021_4_eo-array-element-7070fe.vrt']],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_product', 'extra_values': '[-7.5];list'}}],
                        queue='process'
                        )

sum_8_1 = eoDataReadersOp(task_id='sum_8_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00001-6b931b6e_20180608T101021_20180608T101021_1_eo-array-element-f07f78.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00001-81a9d837_20180608T101021_20180608T101021_1_eo-multiply-0e154a.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00001-438bce77_20180608T101021_20180608T101021_1_eo-multiply-442b0e.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_sum', 'extra_values': '[10000];list'}}],
                        queue='process'
                        )

sum_8_2 = eoDataReadersOp(task_id='sum_8_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00002-f108a3a9_20180611T102021_20180611T102021_2_eo-array-element-ff8efa.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00002-7377e481_20180611T102021_20180611T102021_2_eo-multiply-abe2f7.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00002-f572e31e_20180611T102021_20180611T102021_2_eo-multiply-35ea7f.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_sum', 'extra_values': '[10000];list'}}],
                        queue='process'
                        )

sum_8_3 = eoDataReadersOp(task_id='sum_8_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00003-6c2f0ae7_20180618T101021_20180618T101021_3_eo-array-element-a9a46d.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00003-7995d345_20180618T101021_20180618T101021_3_eo-multiply-b2410f.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00003-0e4d52cc_20180618T101021_20180618T101021_3_eo-multiply-05e111.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_sum', 'extra_values': '[10000];list'}}],
                        queue='process'
                        )

sum_8_4 = eoDataReadersOp(task_id='sum_8_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/00004-1d2e6450_20180621T102021_20180621T102021_4_eo-array-element-ea054d.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/00004-c2846a93_20180621T102021_20180621T102021_4_eo-multiply-aea212.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/00004-64ad4cac_20180621T102021_20180621T102021_4_eo-multiply-b628bb.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_sum', 'extra_values': '[10000];list'}}],
                        queue='process'
                        )

div_9_1 = eoDataReadersOp(task_id='div_9_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00001-7390656f_20180608T101021_20180608T101021_1_eo-subtract-7dbcfe.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00001-0167b364_20180608T101021_20180608T101021_1_eo-sum-c0bdfe.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_divide'}}],
                        queue='process'
                        )

div_9_2 = eoDataReadersOp(task_id='div_9_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00002-32b27b20_20180611T102021_20180611T102021_2_eo-subtract-443546.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00002-ff1e6127_20180611T102021_20180611T102021_2_eo-sum-b75844.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_divide'}}],
                        queue='process'
                        )

div_9_3 = eoDataReadersOp(task_id='div_9_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00003-4954df19_20180618T101021_20180618T101021_3_eo-subtract-6a1885.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00003-de913b37_20180618T101021_20180618T101021_3_eo-sum-c1965e.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_divide'}}],
                        queue='process'
                        )

div_9_4 = eoDataReadersOp(task_id='div_9_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/00004-c631142c_20180621T102021_20180621T102021_4_eo-subtract-85279d.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/00004-18112b24_20180621T102021_20180621T102021_4_eo-sum-0a90bf.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_divide'}}],
                        queue='process'
                        )

p3_10 = eoDataReadersOp(task_id='p3_10',
                        dag=dag,
                        input_filepaths=[['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00001-555fe14d_20180608T101021_20180608T101021_1_eo-divide-fe138e.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00002-9c1fd252_20180611T102021_20180611T102021_2_eo-divide-2de01a.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00003-3f5f478a_20180618T101021_20180618T101021_3_eo-divide-181283.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/00004-1f2bf8d7_20180621T102021_20180621T102021_4_eo-divide-7c4912.vrt']],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}],
                        queue='process'
                        )

evi_1 = eoDataReadersOp(task_id='evi_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/00004-34b970b4_20180621T102021_20180621T102021_4_eo-multiply-4efca0.tif', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/00003-1a401587_20180618T101021_20180618T101021_3_eo-multiply-78ba74.tif', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/00001-482452d0_20180608T101021_20180608T101021_1_eo-multiply-871c38.tif', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/00002-8f8cacf2_20180611T102021_20180611T102021_2_eo-multiply-19b90c.tif'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}],
                        queue='process'
                        )

min_12 = eoDataReadersOp(task_id='min_12',
                        dag=dag,
                        input_filepaths=[['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00001-482452d0_20180608T101021_20180608T101021_1_eo-multiply-871c38.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00002-8f8cacf2_20180611T102021_20180611T102021_2_eo-multiply-19b90c.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00003-1a401587_20180618T101021_20180618T101021_3_eo-multiply-78ba74.vrt', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/00004-34b970b4_20180621T102021_20180621T102021_4_eo-multiply-4efca0.vrt']],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'eo_min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}],
                        queue='process'
                        )

mintime_11 = eoDataReadersOp(task_id='mintime_11',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/00001-bc6537bb_20180608T101021_20180621T102021_5_eo-min-bf9878.tif'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}],
                        queue='process'
                        )

save_13 = eoDataReadersOp(task_id='save_13',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/00001-bc6537bb_20180608T101021_20180621T102021_5_eo-min-bf9878.vrt'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}],
                        queue='process'
                        )

nir_2.set_upstream([dc_0])

red_3.set_upstream([dc_0])

blue_4.set_upstream([dc_0])

sub_5_1.set_upstream([nir_2,red_3])

sub_5_2.set_upstream([nir_2,red_3])

sub_5_3.set_upstream([nir_2,red_3])

sub_5_4.set_upstream([nir_2,red_3])

p1_6.set_upstream([red_3])

p2_7.set_upstream([blue_4])

sum_8_1.set_upstream([nir_2,p1_6,p2_7])

sum_8_2.set_upstream([nir_2,p1_6,p2_7])

sum_8_3.set_upstream([nir_2,p1_6,p2_7])

sum_8_4.set_upstream([nir_2,p1_6,p2_7])

div_9_1.set_upstream([sub_5_1,sum_8_1])

div_9_2.set_upstream([sub_5_2,sum_8_2])

div_9_3.set_upstream([sub_5_3,sum_8_3])

div_9_4.set_upstream([sub_5_4,sum_8_4])

p3_10.set_upstream([div_9_1,div_9_2,div_9_3,div_9_4])

evi_1.set_upstream([p3_10])

min_12.set_upstream([evi_1])

mintime_11.set_upstream([min_12])

save_13.set_upstream([mintime_11])
