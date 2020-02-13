#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for eodc_openeo_bindings.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import os
import pytest
from collections import namedtuple


def get_test_folder():
    return os.getcwd()


@pytest.fixture()
def test_folder():
    return get_test_folder()


@pytest.fixture()
def csw_server():
    os.environ['CSW_SERVER'] = 'https://csw.eodc.eu'


@pytest.fixture()
def evi_file():
    test_folder = get_test_folder()
    return os.path.join(test_folder, 'tests/process_graphs/evi.json')


@pytest.fixture()
def evi_ref_node():
    refNode = namedtuple('RefNode', 'name input_filepaths')
    return [
        refNode('dc', None),
        refNode('blue', ['dc']),
        refNode('p2', ['blue']),
        refNode('red', ['dc']),
        refNode('p1', ['red']),
        refNode('nir', ['dc']),
        refNode('sum', ['nir', 'p1', 'p2']),
        refNode('sub', ['nir', 'red']),
        refNode('div', ['sub', 'sum']),
        refNode('p3', ['div']),
        refNode('evi', ['p3']),
        refNode('min', ['evi']),
        refNode('mintime', ['min']),
        refNode('save', ['mintime'])
    ]
