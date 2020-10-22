import numpy as np

from eodc_openeo_bindings.map_math_processes import *
from eodatareaders.eo_data_reader import EODataProcessor


def test_map_absolute(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "absolute",
        "arguments": {
            "x": {"from_node": "dc"}
        }
    }

    params = map_absolute(process)
    eodatareaders_params.extend(params)

    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)

    assert eo.get_data(band='absolute')[0,0] == 576


def test_map_absolute(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "clip",
        "arguments": {
            "x": {"from_node": "dc"},
            "min": 600,
            "max": 900
        }
    }

    params = map_clip(process)
    eodatareaders_params.extend(params)

    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    assert np.min(eo.get_data(band='clip')) == 600
    assert np.max(eo.get_data(band='clip')) == 900


def test_map_multiply(eodatareaders_file, eodatareaders_params):

    factor = 10
    process = {
        "process_id": "multiply",
        "arguments": {
            "x": {"from_node": "dc"},
            "y": factor
        }
    }
    # process['wrapper_dimension'] = 'band'
    params = map_multiply(process)
    eodatareaders_params.extend(params)

    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    # assert eo.get_data(band='multiplyB04')[0,0] == 576 * factor

    assert eo.get_data(band='multiply')[0,0] == eo.get_data(band='B04')[0,0] * factor
