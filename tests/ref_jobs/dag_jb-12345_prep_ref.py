from datetime import datetime, timedelta
from airflow import DAG
from eodatareaders.eo_data_reader import EODataProcessor
from airflow.operators import PythonOperator

default_args = {
    'owner': "jdoe_67890",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "None",
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(dag_id="jb-12345_prep",
          description="No description provided",
          catchup=True,
          max_active_runs=1,
          schedule_interval=None,
          default_args=default_args)

dc_0 = PythonOperator(task_id='dc_0',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': ['/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip', '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip', '/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip', '/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip', '/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip', '/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip', '/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip'], 'dc_filepaths': None, 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/dc_0/'}, {'name': 'filter_bands', 'bands': ['B08', 'B04', 'B02']}, {'name': 'crop', 'extent': (11.279182434082033, 46.464349400461145, 11.406898498535158, 46.522729291844286), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': '/openeo_job/dc_0/dc_0.dc;str'}]},
                        queue='process'
                        )

nir_2 = PythonOperator(task_id='nir_2',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/dc_0/dc_0.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/nir_2/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '0;int'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/nir_2/nir_2.dc;str'}]},
                        queue='process'
                        )

red_3 = PythonOperator(task_id='red_3',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/dc_0/dc_0.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/red_3/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '1;int'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/red_3/red_3.dc;str'}]},
                        queue='process'
                        )

blue_4 = PythonOperator(task_id='blue_4',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/dc_0/dc_0.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/blue_4/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'array_element', 'index': '2;int'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/blue_4/blue_4.dc;str'}]},
                        queue='process'
                        )

sub_5 = PythonOperator(task_id='sub_5',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/nir_2/nir_2.dc', '/openeo_job/red_3/red_3.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/sub_5/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'subtract', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/sub_5/sub_5.dc;str'}]},
                        queue='process'
                        )

p1_6 = PythonOperator(task_id='p1_6',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/red_3/red_3.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/p1_6/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[6];list'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/p1_6/p1_6.dc;str'}]},
                        queue='process'
                        )

p2_7 = PythonOperator(task_id='p2_7',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/blue_4/blue_4.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/p2_7/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[-7.5];list'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/p2_7/p2_7.dc;str'}]},
                        queue='process'
                        )

sum_8 = PythonOperator(task_id='sum_8',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/nir_2/nir_2.dc', '/openeo_job/p1_6/p1_6.dc', '/openeo_job/p2_7/p2_7.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/sum_8/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'sum', 'extra_values': '[10000];list'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/sum_8/sum_8.dc;str'}]},
                        queue='process'
                        )

div_9 = PythonOperator(task_id='div_9',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/sub_5/sub_5.dc', '/openeo_job/sum_8/sum_8.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/div_9/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'divide', 'y': 'set;str'}}, {'name': 'to_pickle', 'filepath': '/openeo_job/div_9/div_9.dc;str'}]},
                        queue='process'
                        )

p3_10 = PythonOperator(task_id='p3_10',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/div_9/div_9.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/p3_10/'}, {'name': 'reduce', 'dimension': 'band', 'f_input': {'f_name': 'product', 'extra_values': '[2.5];list'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/openeo_job/p3_10/p3_10.dc;str'}]},
                        queue='process'
                        )

evi_1 = PythonOperator(task_id='evi_1',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/p3_10/p3_10.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/evi_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/openeo_job/evi_1/evi_1.dc;str'}]},
                        queue='process'
                        )

min_12 = PythonOperator(task_id='min_12',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/evi_1/evi_1.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/min_12/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'min'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': '/openeo_job/min_12/min_12.dc;str'}]},
                        queue='process'
                        )

mintime_11 = PythonOperator(task_id='mintime_11',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/min_12/min_12.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/mintime_11/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': '/openeo_job/mintime_11/mintime_11.dc;str'}]},
                        queue='process'
                        )

save_13 = PythonOperator(task_id='save_13',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['/openeo_job/mintime_11/mintime_11.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': '/openeo_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': '/openeo_job/result/save_13.dc;str'}]},
                        queue='process'
                        )

nir_2.set_upstream([dc_0])

red_3.set_upstream([dc_0])

blue_4.set_upstream([dc_0])

sub_5.set_upstream([nir_2,red_3])

p1_6.set_upstream([red_3])

p2_7.set_upstream([blue_4])

sum_8.set_upstream([nir_2,p1_6,p2_7])

div_9.set_upstream([sub_5,sum_8])

p3_10.set_upstream([div_9])

evi_1.set_upstream([p3_10])

min_12.set_upstream([evi_1])

mintime_11.set_upstream([min_12])

save_13.set_upstream([mintime_11])
