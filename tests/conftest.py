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
def csw_server():
    os.environ['CSW_SERVER'] = 'http://pycsw:8000'


@pytest.fixture()
def acube_csw_server():
    os.environ['ACUBE_CSW_SERVER'] = 'https://csw-acube.eodc.eu/'


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
def setup_ref_job_folder(request):
    test_folder = get_test_folder()
    os.environ['REF_JOBS'] = os.path.join(test_folder, 'ref_jobs')


@pytest.fixture()
def airflow_job_folder():
    return os.path.join(get_test_folder(), 'ref_airflow_job')
