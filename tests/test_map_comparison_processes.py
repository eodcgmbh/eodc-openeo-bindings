import numpy as np

from eodc_openeo_bindings.map_comparison_processes import *
from eodatareaders.eo_data_reader import EODataProcessor


def test_map_lt(eodatareaders_file, eodatareaders_params):

    process = {
        "process_id": "lt",
        "arguments": {
            "x": {"from_node": "node_1"},
            "y": 1000,
        }
    }

    params = map_lt(process)
    eodatareaders_params.extend(params)
    eo = EODataProcessor([eodatareaders_file], eodatareaders_params)
    assert eo.get_data(band='B04')[0,0] == 576 and eo.get_data(band='lt')[0,0] == 1
    assert eo.get_data(band='B04')[-1,-1] == 2567 and eo.get_data(band='lt')[-1,-1] == 0
