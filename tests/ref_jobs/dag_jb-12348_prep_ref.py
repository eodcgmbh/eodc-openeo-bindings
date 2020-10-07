from datetime import datetime, timedelta
from airflow import DAG
from airflow.hooks.base_hook import BaseHook
from eodatareaders.eo_data_reader import EODataProcessor
from airflow.operators import PythonOperator, CancelOp, StopDagOp

default_args = {
    'owner': "jdoe_67890",
    'depends_on_past': False,
    'start_date': datetime.combine(datetime.today() - timedelta(1), datetime.min.time()),
    'email': "None",
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(dag_id="jb-12348_prep",
          description="No description provided",
          catchup=True,
          max_active_runs=1,
          schedule_interval=None,
          default_args=default_args)

load_collection_0 = PythonOperator(task_id='load_collection_0',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': ['./wekeo_data_storage/S5P_RPRO_L2__NO2____20180503T093059_20180503T111427_02866_01_010202_20190202T034117.nc', './wekeo_data_storage/S5P_RPRO_L2__NO2____20180502T094957_20180502T113325_02852_01_010202_20190201T215849.nc', './wekeo_data_storage/S5P_RPRO_L2__NO2____20180501T082724_20180501T101003_02837_01_010202_20190201T175639.nc'], 'dc_filepaths': None, 'user_params': [{'name': 'set_output_folder', 'out_dirpath': './openeo_job/load_collection_0/'}, {'name': 'filter_bands', 'bands': ['NO2']}, {'name': 'quick_geocode', 'scale_sampling': '1;int'}, {'name': 'crop', 'extent': (16.06, 48.06, 16.65, 48.35), 'crs': 'EPSG:4326'}, {'name': 'to_pickle', 'filepath': './openeo_job/load_collection_0/load_collection_0.dc;str'}]},
                        queue='process'
                        )

mean_2 = PythonOperator(task_id='mean_2',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['./openeo_job/load_collection_0/load_collection_0.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': './openeo_job/mean_2/'}, {'name': 'reduce', 'dimension': 'time', 'f_input': {'f_name': 'mean'}}, {'name': 'save_raster', 'in_place': 'True;bool', 'format_type': 'Gtiff'}, {'name': 'to_pickle', 'filepath': './openeo_job/mean_2/mean_2.dc;str'}]},
                        queue='process'
                        )

t_mean_1 = PythonOperator(task_id='t_mean_1',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['./openeo_job/mean_2/mean_2.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': './openeo_job/t_mean_1/'}, {'name': 'save_raster', 'format_type': 'VRT'}, {'name': 'to_pickle', 'filepath': './openeo_job/t_mean_1/t_mean_1.dc;str'}]},
                        queue='process'
                        )

save_result_3 = PythonOperator(task_id='save_result_3',
                        dag=dag,
                        python_callable=EODataProcessor,
                        op_kwargs={'filepaths': None, 'dc_filepaths': ['./openeo_job/t_mean_1/t_mean_1.dc'], 'user_params': [{'name': 'set_output_folder', 'out_dirpath': './openeo_job/result/'}, {'name': 'save_raster'}, {'name': 'get_cube_metadata'}, {'name': 'to_pickle', 'filepath': './openeo_job/result/save_result_3.dc;str'}]},
                        queue='process'
                        )

mean_2.set_upstream([load_collection_0])

t_mean_1.set_upstream([mean_2])

save_result_3.set_upstream([t_mean_1])


cancel_sensor = CancelOp(task_id='cancel_sensor',
                         dag=dag,
                         stop_file='./openeo_job/STOP',
                         queue='sensor',
                         )

stop_dag = StopDagOp(task_id='stop_dag', dag=dag, queue='process')
stop_dag.set_upstream([cancel_sensor])


def download_wekeo_data(wekeo_job_id, item_url, output_filepath):

    import os
    import requests
    import zipfile

    output_filepath_zip = output_filepath + ".zip"
    output_filepath_nc = output_filepath + ".nc"
    f_name = os.path.basename(output_filepath)
    f_dir = os.path.dirname(output_filepath)

    # Get token
    response = requests.get(BaseHook.get_connection('wekeo_hda').host + "/gettoken",
                            auth=(BaseHook.get_connection("wekeo_hda").login,
                                  BaseHook.get_connection("wekeo_hda").password
                            )
                )
    if not response.ok:
        raise Exception(response.text)
    access_token = response.json()["access_token"]
    service_headers = {
            "Authorization": "Bearer " + access_token,
            "Accept": "application/json"
        }
    # Create a WEkEO dataorder
    response2 = requests.post(BaseHook.get_connection('wekeo_hda').host + "/dataorder",
                              json={"jobId": wekeo_job_id, "uri": item_url},
                              headers=service_headers)
    if not response2.ok:
        raise Exception(response2.text)
    # check dataorder status
    order_id = response2.json()["orderId"]
    while not response2.json()["message"]:
        response2 = requests.get(BaseHook.get_connection('wekeo_hda').host + "/dataorder/status/" + order_id,
                                 headers=service_headers)
    if not os.path.isfile(output_filepath_nc):
        # Download file
        response3 = requests.get(BaseHook.get_connection('wekeo_hda').host + "/dataorder/download/" + order_id,
                                 headers=service_headers, stream=True)
        if not response3.ok:
            raise Exception(response3.text)
        with open(output_filepath_zip, "wb") as f:
            for chunk in response3.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        # Unzip file
        with zipfile.ZipFile(output_filepath_zip,"r") as zip_ref:
            zip_ref.extractall(f_dir)
        # Move extracted files 'one folder up'
        os.rename(os.path.join(output_filepath, f_name + ".nc"), os.path.join(f_dir, f_name + ".nc"))
        os.rename(os.path.join(output_filepath, f_name + ".cdl"), os.path.join(f_dir, f_name + ".cdl"))
        # Remove zip file and empty folder
        os.remove(output_filepath_zip)
        os.rmdir(output_filepath)

wekeo_0 = PythonOperator(task_id='wekeo_download_0',
                                 dag=dag,
                                 python_callable=download_wekeo_data,
                                 op_kwargs = {'wekeo_job_id': 'EGUIBC37kepM90lTGVNTHpIdfuA', 'item_url': '6a143583-a6a4-53e6-9e6d-8d4edc60a702/S5P_RPRO_L2__NO2____20180503T093059_20180503T111427_02866_01_010202_20190202T034117', 'output_filepath': './wekeo_data_storage/S5P_RPRO_L2__NO2____20180503T093059_20180503T111427_02866_01_010202_20190202T034117'},
                                 queue='process')
wekeo_0.set_downstream([load_collection_0])
    
wekeo_1 = PythonOperator(task_id='wekeo_download_1',
                                 dag=dag,
                                 python_callable=download_wekeo_data,
                                 op_kwargs = {'wekeo_job_id': 'EGUIBC37kepM90lTGVNTHpIdfuA', 'item_url': '08ef0029-4d75-5821-8cf8-b4def8b89306/S5P_RPRO_L2__NO2____20180502T094957_20180502T113325_02852_01_010202_20190201T215849', 'output_filepath': './wekeo_data_storage/S5P_RPRO_L2__NO2____20180502T094957_20180502T113325_02852_01_010202_20190201T215849'},
                                 queue='process')
wekeo_1.set_downstream([load_collection_0])
    
wekeo_2 = PythonOperator(task_id='wekeo_download_2',
                                 dag=dag,
                                 python_callable=download_wekeo_data,
                                 op_kwargs = {'wekeo_job_id': 'EGUIBC37kepM90lTGVNTHpIdfuA', 'item_url': '7e0e3654-5447-5f5d-be1d-5bf61dd72be8/S5P_RPRO_L2__NO2____20180501T082724_20180501T101003_02837_01_010202_20190201T175639', 'output_filepath': './wekeo_data_storage/S5P_RPRO_L2__NO2____20180501T082724_20180501T101003_02837_01_010202_20190201T175639'},
                                 queue='process')
wekeo_2.set_downstream([load_collection_0])
   