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
from collections import namedtuple

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
def setup_airflow_dag_folder(request):
    test_folder = get_test_folder()
    os.environ['AIRFLOW_DAGS'] = os.path.join(test_folder, 'airflow_dag')
    if os.path.isdir(os.environ['AIRFLOW_DAGS']):
        shutil.rmtree(os.environ['AIRFLOW_DAGS'])
    os.makedirs(os.environ['AIRFLOW_DAGS'])

    def fin():
        shutil.rmtree(os.environ['AIRFLOW_DAGS'])

    request.addfinalizer(fin)


@pytest.fixture()
def setup_ref_job_folder():
    os.environ['REF_JOBS'] = os.path.join(get_test_folder(), 'ref_jobs')


@pytest.fixture()
def airflow_job_folder():
    return os.path.join(get_test_folder(), 'ref_airflow_job')


@pytest.fixture()
def csw_server_default(mocker):
    csw_server_response = [
        '/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip',
        '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip',
        '/s2a_prd_msil1c/2018/06/18/S2A_MSIL1C_20180618T101021_N0206_R022_T32TPS_20180618T135619.zip',
        '/s2a_prd_msil1c/2018/06/21/S2A_MSIL1C_20180621T102021_N0206_R065_T32TPS_20180621T140615.zip',
        '/s2b_prd_msil1c/2018/06/06/S2B_MSIL1C_20180606T102019_N0206_R065_T32TPS_20180606T172808.zip',
        '/s2b_prd_msil1c/2018/06/13/S2B_MSIL1C_20180613T101019_N0206_R022_T32TPS_20180613T122213.zip',
        '/s2b_prd_msil1c/2018/06/16/S2B_MSIL1C_20180616T102019_N0206_R065_T32TPS_20180616T154713.zip',
    ]
    mocker.patch('eodc_openeo_bindings.map_cubes_processes.csw_query', return_value=csw_server_response)


@pytest.fixture()
def acube_csw_server_default(mocker):
    csw_server_response = [
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050118--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N015T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050118--_EU010M_E052N015T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_050935--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VHD_20170301_051000--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_050935--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1A_IWGRDH1VVD_20170301_051000--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050028--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VHD_20170302_050053--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050028--_EU010M_E052N016T1.tif',
        '/eodc/products/ADatacube/Sentinel-1_CSAR/IWGRDH/preprocessed/datasets/resampled/A0105/EQUI7_EU010M/E052N016T1/sig0/SIG0-----_SGRTA01_S1B_IWGRDH1VVD_20170302_050053--_EU010M_E052N016T1.tif',
    ]
    mocker.patch('eodc_openeo_bindings.map_cubes_processes.csw_query', return_value=csw_server_response)
