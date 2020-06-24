from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import eoDataReadersOp, CancelOp, StopDagOp

default_args = {
    'owner': "jdoe_67890",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "None",
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(dag_id="jb-12345_delete_sensor",
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

blue_4 = eoDataReadersOp(task_id='blue_4',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_array_element', 'index': '2;int'}}],
                        queue='process'
                        )

p2_7 = eoDataReadersOp(task_id='p2_7',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/blue_4/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_product', 'extra_values': '[-7.5];list'}}],
                        queue='process'
                        )

red_3 = eoDataReadersOp(task_id='red_3',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_array_element', 'index': '1;int'}}],
                        queue='process'
                        )

p1_6 = eoDataReadersOp(task_id='p1_6',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_product', 'extra_values': '[6];list'}}],
                        queue='process'
                        )

nir_2 = eoDataReadersOp(task_id='nir_2',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/dc_0/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_array_element', 'index': '0;int'}}],
                        queue='process'
                        )

sum_8 = eoDataReadersOp(task_id='sum_8',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p1_6/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p2_7/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_sum', 'extra_values': '[10000];list'}}],
                        queue='process'
                        )

sub_5 = eoDataReadersOp(task_id='sub_5',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/nir_2/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/red_3/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_subtract'}}],
                        queue='process'
                        )

div_9 = eoDataReadersOp(task_id='div_9',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sub_5/', '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/sum_8/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_divide'}}],
                        queue='process'
                        )

p3_10 = eoDataReadersOp(task_id='p3_10',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/div_9/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'eo_product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}],
                        queue='process'
                        )

evi_1 = eoDataReadersOp(task_id='evi_1',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/p3_10/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}],
                        queue='process'
                        )

min_12 = eoDataReadersOp(task_id='min_12',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/evi_1/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'eo_min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}],
                        queue='process'
                        )

mintime_11 = eoDataReadersOp(task_id='mintime_11',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/min_12/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}],
                        queue='process'
                        )

save_13 = eoDataReadersOp(task_id='save_13',
                        dag=dag,
                        input_filepaths=['/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/mintime_11/'],
                        input_params=[{'name': 'set_output_folder', 'out_dirpath': '/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/result/'}, {'name': 'save_raster'}],
                        queue='process'
                        )

blue_4.set_upstream([dc_0])

p2_7.set_upstream([blue_4])

red_3.set_upstream([dc_0])

p1_6.set_upstream([red_3])

nir_2.set_upstream([dc_0])

sum_8.set_upstream([nir_2,p1_6,p2_7])

sub_5.set_upstream([nir_2,red_3])

div_9.set_upstream([sub_5,sum_8])

p3_10.set_upstream([div_9])

evi_1.set_upstream([p3_10])

min_12.set_upstream([evi_1])

mintime_11.set_upstream([min_12])

save_13.set_upstream([mintime_11])


cancel_sensor = CancelOp(task_id='cancel_sensor',
                         dag=dag,
                         stop_file='/home/luca/eodc/repos/openeo/eodc-openeo-bindings/tests/openeo_job/STOP',
                         queue='sensor',
                         )

stop_dag = StopDagOp(task_id='stop_dag', dag=dag, queue='process')
stop_dag.set_upstream([cancel_sensor])
