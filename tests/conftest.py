#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for eodc_openeo_bindings.
    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import os
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
def evi_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'process_graphs', 'evi.json')


@pytest.fixture()
def evi_ref_node():
    refNode = namedtuple('RefNode', 'name input_filepaths')
    return [
        refNode('dc', None),
        refNode('nir', ['dc']),
        refNode('red', ['dc']),
        refNode('sub', ['nir', 'red']),
        refNode('p1', ['red']),
        refNode('blue', ['dc']),
        refNode('p2', ['blue']),
        refNode('sum', ['nir', 'p1', 'p2']),
        refNode('div', ['sub', 'sum']),
        refNode('p3', ['div']),
        refNode('evi', ['p3']),
        refNode('min', ['evi']),
        refNode('mintime', ['min']),
        refNode('save', ['mintime'])
    ]


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
def airflow_job_folder():
    return os.path.join(get_test_folder(), 'ref_airflow_job')
