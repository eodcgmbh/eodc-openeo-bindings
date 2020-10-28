#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for eodc_openeo_bindings.
    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import os
import json
import shutil
import subprocess
import pytest


def get_test_folder():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def test_folder():
    return get_test_folder()


@pytest.fixture()
def evi_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'evi.json')

@pytest.fixture()
def wekeo_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'wekeo.json')

@pytest.fixture()
def uc1_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'UC1.json')


@pytest.fixture()
def uc1_temporal_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'UC1_temporal.json')


@pytest.fixture()
def uc1_spectral_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'UC1_spectral.json')


@pytest.fixture()
def apply_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'apply_job.json')


@pytest.fixture()
def out_filepath_basic(request):
    path = os.path.join(get_test_folder(), 'basic_job.py')

    def fin():
        if os.path.isfile(path):
            os.remove(path)
    request.addfinalizer(fin)
    return path


@pytest.fixture()
def out_filepath_basic_apply(request):
    path = os.path.join(get_test_folder(), 'basic_job_apply.py')

    def fin():
        if os.path.isfile(path):
            os.remove(path)
    request.addfinalizer(fin)
    return path


@pytest.fixture()
def backend_processes():
    test_folder = get_test_folder()
    return json.load(open(os.path.join(test_folder, 'backend_processes.json')))['processes']


@pytest.fixture()
def airflow_dag_folder(request):
    test_folder = get_test_folder()
    dags_folder = os.path.join(test_folder, 'airflow_dag')
    if os.path.isdir(dags_folder):
        shutil.rmtree(dags_folder)
    os.makedirs(dags_folder)

    def fin():
        shutil.rmtree(dags_folder)

    request.addfinalizer(fin)

    return dags_folder


@pytest.fixture()
def setup_ref_job_folder():
    os.environ['REF_JOBS'] = os.path.join(get_test_folder(), 'ref_jobs')


@pytest.fixture()
def airflow_job_folder():
    return os.path.join(get_test_folder(), 'ref_airflow_job')


@pytest.fixture()
def S2_filepaths():
    return {
        'dc': {
            'filepaths': [
                '/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip',
                '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip',
                '/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip',
                '/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip',
                '/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip',
                '/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip',
                '/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip',
            ]
        }
    }

@pytest.fixture()
def S2_filepaths_short():
    return {
        'dc': {
            'filepaths': [
                '/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip',
                '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip'
            ]
        }
    }

@pytest.fixture()
def ACube_filepaths():
    output = {
        'filepaths': [
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050118--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050118--_EU010M_E052N015T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050028--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050028--_EU010M_E052N016T1.tif',
            'sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N016T1.tif',
        ]
    }
    return {
        'load_collection': output,
        'march': output,
        'april': output,
        'may': output
    }

@pytest.fixture()
def wekeo_filepaths():
    wekeo_dict = {
        'load_collection': {
            'filepaths': [
                '6a143583-a6a4-53e6-9e6d-8d4edc60a702/S5P_RPRO_L2__NO2____20180503T093059_20180503T111427_02866_01_010202_20190202T034117',
                '08ef0029-4d75-5821-8cf8-b4def8b89306/S5P_RPRO_L2__NO2____20180502T094957_20180502T113325_02852_01_010202_20190201T215849',
                '7e0e3654-5447-5f5d-be1d-5bf61dd72be8/S5P_RPRO_L2__NO2____20180501T082724_20180501T101003_02837_01_010202_20190201T175639'
            ],
            'wekeo_job_id': 'EGUIBC37kepM90lTGVNTHpIdfuA'
        }
    }

    return wekeo_dict


@pytest.fixture()
def eodatareaders_params(request):
    job_folder = '/tmp/output_folder/'
    params = [
        {'name': 'set_output_folder', 'out_dirpath': job_folder},
        {'name': 'filter_bands', 'bands': ['B04']},
        {'name': 'crop', 'extent': (11.28, 46.52, 11.41, 46.46), 'crs': 'EPSG:4326'}
    ]
    
    def fin():
        shutil.rmtree(job_folder)

    request.addfinalizer(fin)

    return params


@pytest.fixture()
def eodatareaders_file():
    filename = "S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip"
    test_file = f"/tmp/{filename}"
    if not os.path.isfile(test_file):
        subprocess.call(["wget", f"https://openeo.eodc.eu/test-files/{filename}"])
        os.rename(filename, test_file)
    os.environ["GDAL_VRT_ENABLE_PYTHON"] = 'TRUSTED_MODULES'
    os.environ["GDAL_VRT_PYTHON_TRUSTED_MODULES"] = 'eodatareaders.pixel_functions.pixel_functions'
    return test_file
