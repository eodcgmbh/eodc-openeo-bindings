""" Utils functions to send HTTP requests to WEkEO HDA API """

import os
import requests
import zipfile


def wrap_request(func):
    def wrapper_func(*args, **kwargs):
        credentials = kwargs.pop('credentials')
        kwargs['headers'] = request_wekeo_token(**credentials)
        response = func(**kwargs)
        if response.status_code == 403:
            # Token has expired, get new one and repeat request
            kwargs['headers'] = request_wekeo_token(*kwargs)
            response = func(**kwargs)
        if not response.ok:
            raise Exception(response.text)

        return response
    return wrapper_func


def request_wekeo_token(wekeo_url, username, password):

    response = requests.get(wekeo_url + "/gettoken", auth=(username, password))
    if not response.ok:
        raise Exception(response.text)
    return {
            "Authorization": "Bearer " + response.json()["access_token"],
            "Accept": "application/json"
        }


@wrap_request
def request_wekeo_dataorder(wekeo_url, wekeo_job_id, item_url, headers):

    response = requests.post(wekeo_url + "/dataorder",
                              json={"jobId": wekeo_job_id, "uri": item_url},
                              headers=headers)

    return response


@wrap_request
def request_check_order_status(order_id_url, headers):

    response = requests.get(order_id_url, headers=headers)

    return response


@wrap_request
def request_download(order_id_url, headers):

    response = requests.get(order_id_url, headers=headers, stream=True)
    if not response.ok:
        raise Exception(response.text)

    return response


def download_wekeo_data(wekeo_url, username, password,
                        wekeo_job_id, item_url, output_filepath):

    # Setup filenames
    output_filepath_zip = output_filepath + ".zip"
    output_filepath_nc = output_filepath + ".nc"
    f_name = os.path.basename(output_filepath)
    f_dir = os.path.dirname(output_filepath)

    credentials = {
        'wekeo_url': wekeo_url,
        'username': username,
        'password': password
    }

    # Create a WEkEO dataorder
    response = request_wekeo_dataorder(credentials=credentials,
                                       wekeo_url=credentials['wekeo_url'],
                                       wekeo_job_id=wekeo_job_id,
                                       item_url=item_url)
    order_id_url = credentials['wekeo_url'] + "/dataorder/status/" + \
        response.json()["orderId"]

    # Check dataorder status
    response = request_check_order_status(credentials=credentials, order_id_url=order_id_url)
    while not response.json()["message"]:
        response = request_check_order_status(credentials=credentials, order_id_url=order_id_url)

    # Download file
    if not os.path.isfile(output_filepath_nc):
        response = request_download(credentials=credentials, order_id_url=order_id_url)

        with open(output_filepath_zip, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
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
