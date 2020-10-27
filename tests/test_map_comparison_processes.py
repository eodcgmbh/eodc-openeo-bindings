from copy import deepcopy
import numpy as np

from eodc_openeo_bindings.map_comparison_processes import *
from eodatareaders.eo_data_reader import EODataProcessor


def test_map_lt(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "lt",
        "arguments": {
            "x": {"from_node": "node_1"},
            "y": 567,
        }
    }

    params = map_lt(process)
    eodatareaders_params.extend(params)
    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    assert eo.get_data(band='B04')[0,0] == 576 and eo.get_data(band='lt')[0,0] == 0
    assert eo.get_data(band='B04')[-1,-1] == 2567 and eo.get_data(band='lt')[-1,-1] == 0


def test_map_lte(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "lte",
        "arguments": {
            "x": {"from_node": "node_1"},
            "y": 576,
        }
    }

    params = map_lte(process)
    eodatareaders_params.extend(params)
    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    assert eo.get_data(band='B04')[0,0] == 576 and eo.get_data(band='lte')[0,0] == 1
    assert eo.get_data(band='B04')[-1,-1] == 2567 and eo.get_data(band='lte')[-1,-1] == 0


def test_map_gt(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "gt",
        "arguments": {
            "x": {"from_node": "node_1"},
            "y": 576,
        }
    }

    params = map_gt(process)
    eodatareaders_params.extend(params)
    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    assert eo.get_data(band='B04')[0,0] == 576 and eo.get_data(band='gt')[0,0] == 0
    assert eo.get_data(band='B04')[-1,-1] == 2567 and eo.get_data(band='gt')[-1,-1] == 1


def test_map_gte(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "gte",
        "arguments": {
            "x": {"from_node": "node_1"},
            "y": 576,
        }
    }

    params = map_gte(process)
    eodatareaders_params.extend(params)
    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    assert eo.get_data(band='B04')[0,0] == 576 and eo.get_data(band='gte')[0,0] == 1
    assert eo.get_data(band='B04')[-1,-1] == 2567 and eo.get_data(band='gte')[-1,-1] == 1


def test_map_eq(eodatareaders_file, eodatareaders_params):

    process = [
        {
            "process_id": "eq",
            "arguments": {
                "x": {"from_node": "node_1"},
                "y": 576,
            }
        },
        {
            "process_id": "eq",
            "arguments": {
                "x": {"from_node": "node_1"},
                "y": 577,
                "delta": 1
            }
        }
    ]

    for proc in process:
        eodatareaders_params2 = deepcopy(eodatareaders_params)
        params = map_eq(proc)
        eodatareaders_params2.extend(params)
        eo = EODataProcessor([eodatareaders_file], eodatareaders_params2)
        assert eo.get_data(band='B04')[0,0] == 576 and eo.get_data(band='eq')[0,0] == 1
