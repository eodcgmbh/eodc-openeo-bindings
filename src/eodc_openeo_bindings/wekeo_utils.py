""" Utils functions to send HTTP requests to WEkEO HDA API """

import os
import requests
import zipfile


def request_wekeo_token(wekeo_url, username, password):

    response = requests.get(wekeo_url + "/gettoken", auth=(username, password))
    if not response.ok:
        raise Exception(response.text)
    return {
            "Authorization": "Bearer " + "5946b682-c8d9-3635-9e91-43a4beb98000",
            #"Authorization": "Bearer " + response.json()["access_token"],
            "Accept": "application/json"
        }


def request_wekeo_dataorder(wekeo_url, wekeo_job_id, item_url, headers):

    response = requests.post(wekeo_url + "/dataorder",
                              json={{"jobId": wekeo_job_id, "uri": item_url}},
                              headers=headers)
    if not response.ok:
        raise Exception(response.text)

    order_id_url = wekeo_url + "/dataorder/status/" + response.json()["orderId"]

    return order_id_url


def request_check_order_status(order_id_url, headers):

    response = requests.get(order_id_url, headers=headers)
    if not response.ok:
        raise Exception(response.text)
    while not response.json()["message"]:
        response = requests.get(order_id_url, headers=headers)
        if not response.ok:
            raise Exception(response.text)

    # no need to return as long as "message" is present in response


def request_download(order_id_url, headers):

    response = requests.get(order_id_url, headers=headers, stream=True)
    if not response.ok:
        raise Exception(response.text)

    return response


def wrap_request(func):
    def wrapper_func(*args, **kwargs):
        kwargs['headers'] = request_wekeo_token()
        response = func(*args, **kwargs)
        if response.status_code == 403:
            # Token has expired, get new one and repeat request
            kwargs['headers'] = request_wekeo_token()
            response = func(*args, **kwargs)
        if not response.ok:
            kwargs['headers'] = request_wekeo_token()

        response = func(*args, **kwargs)

        return response
    return wrapper_func


def download_wekeo_data(wekeo_job_id, item_url, output_filepath):

    # Decorate functions (because of WEkEO tokens lasting 1hour)
    request_wekeo_dataorder = wrap_request(request_wekeo_dataorder)
    request_check_order_status = wrap_request(request_check_order_status)
    request_download = wrap_request(request_download)

    # Setup filenames
    output_filepath_zip = output_filepath + ".zip"
    output_filepath_nc = output_filepath + ".nc"
    f_name = os.path.basename(output_filepath)
    f_dir = os.path.dirname(output_filepath)

    # Get token
    headers = request_wekeo_token()

    # Create a WEkEO dataorder
    order_id_url = request_wekeo_dataorder(wekeo_job_id, item_url)

    # Check dataorder status
    _ = request_check_order_status(order_id_url)

    # Download file
    if not os.path.isfile(output_filepath_nc):
        response = request_download(order_id_url)

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
