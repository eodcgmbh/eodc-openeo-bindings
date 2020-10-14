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
def request_collection_metadata(wekeo_url: str, collection_id: str, headers: dict):

    response = requests.get(f"{wekeo_url}/querymetadata/{collection_id}",
                            headers=headers)
    return response


def create_data_descriptor(collection_id: str, var_id: str, spatial_extent: dict, temporal_extent: list) -> dict:
    """ """

    # Create WEkEO 'data descriptor'
    data_descriptor = {
        "datasetId": collection_id,
        "boundingBoxValues": [
            {
                "name": "bbox",
                "bbox": spatial_extent
            }
        ],
        "dateRangeSelectValues": [
            {
                "name": "position",
                "start": temporal_extent[0],
                "end": temporal_extent[1]
            }
        ],
        "stringChoiceValues": [
            {
                "name": "processingLevel",
                "value": "LEVEL2"
            },
            {
                "name": "productType",
                "value": var_id
            }
        ]
    }

    return data_descriptor


@wrap_request
def create_datarequest(wekeo_url: str, data_descriptor: dict, headers: dict) -> str:
    """ """

    # Create a WEkEO 'datarequest'
    response = requests.post(f"{wekeo_url}/datarequest",
                             json=data_descriptor,
                             headers=headers)
    return response


@wrap_request
def request_wekeo_dataorder(wekeo_url, wekeo_job_id, item_url, headers):

    response = requests.post(wekeo_url + "/dataorder",
                             json={"jobId": wekeo_job_id, "uri": item_url},
                             headers=headers)

    return response


@wrap_request
def get_download_urls(download_url: str, header: dict):
    """ """

    response = requests.get(download_url, headers=headers)

    return response


def _get_download_urls(response):

    download_urls = []
    next_page_url = response.json()['nextPage']
    for item in response.json()['content']:
        download_urls.append(item['url'])

    return download_urls, next_page_url


@wrap_request
def request_check_order_status(order_id_status_url, headers):

    response = requests.get(order_id_status_url, headers=headers)

    return response


@wrap_request
def request_download(order_id_download_url, headers):

    response = requests.get(order_id_download_url, headers=headers, stream=True)
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
    order_id = response.json()["orderId"]
    order_id_status_url = credentials['wekeo_url'] + "/dataorder/status/" + order_id
    order_id_download_url = credentials['wekeo_url'] + "/dataorder/download/" + order_id

    # Check dataorder status
    response = request_check_order_status(credentials=credentials, order_id_status_url=order_id_status_url)
    while not response.json()["message"]:
        response = request_check_order_status(credentials=credentials, order_id_status_url=order_id_status_url)

    # Download file
    if not os.path.isfile(output_filepath_nc):
        response = request_download(credentials=credentials, order_id_download_url=order_id_download_url)

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


def get_filepaths(wekeo_url: str, username: str, password: str,
                  wekeo_data_id: str, wekeo_var_id: str, spatial_extent: dict, temporal_extent: list):
    """Retrieves a URL list from the WEkEO HDA according to the specified parameters.

    Arguments:
        collecion_id {str} -- identifier of the collection
        spatial_extent {List[float]} -- bounding box [ymin, xmin, ymax, ymax]
        temporal_extent {List[str]} -- e.g. ["2018-06-04", "2018-06-23"]

    Returns:
        list -- list of URLs / filepaths
    """

    credentials = {
        'wekeo_url': wekeo_url,
        'username': username,
        'password': password
    }

    # Create Data Descriptor
    data_descriptor = create_data_descriptor(wekeo_data_id, wekeo_var_id, spatial_extent, temporal_extent)

    # Create a Data Request job
    response = create_datarequest(credentials=credentials,
                                  wekeo_url=credentials['wekeo_url'],
                                  data_descriptor=data_descriptor)
    while not response.json()['message']:
        response = create_datarequest(credentials=credentials,
                                      wekeo_url=credentials['wekeo_url'],
                                      data_descriptor=data_descriptor)
    job_id = response.json()['jobId']
    download_url = credentials['wekeo_url'] + f"/datarequest/jobs/{job_id}/result"

    # Get URLs for individual files
    response = get_download_urls(download_url=download_url)
    filepaths, next_page_url = _get_download_urls(response)
    while next_page_url:
        response = get_download_urls(download_url=next_page_url)
        tmp_filepaths, next_page_url = _get_download_urls(response)
        filepaths.extend(tmp_filepaths)

    return filepaths, job_id


def get_collection_metadata(wekeo_url: str, username: str, password: str,
                            collection_id: str):

    credentials = {
        'wekeo_url': wekeo_url,
        'username': username,
        'password': password
    }

    return request_collection_metadata(credentials=credentials,
                                       wekeo_url=credentials['wekeo_url'],
                                       collection_id=collection_id)
