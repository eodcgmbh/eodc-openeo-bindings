from copy import deepcopy
import numpy as np

from eodc_openeo_bindings.map_array_processes import *
from eodc_openeo_bindings.map_comparison_processes import map_lt
from eodatareaders.eo_data_reader import EODataProcessor


def create_mask(eodatareaders_file, eodatareaders_params):
    
    eodatareaders_params_0 = deepcopy(eodatareaders_params)
    eodatareaders_params_0[0]['out_dirpath'] = eodatareaders_params_0[0]['out_dirpath'] + 'lt'
    process = {
        "process_id": "lt",
        "arguments": {
            "x": {"from_node": "node_1"},
            "y": 1000,
        }
    }

    params = map_lt(process)
    eodatareaders_params_0.extend(params)
    eo = EODataProcessor([eodatareaders_file], eodatareaders_params_0)
    return eo.inventory.iloc[0].filepath, eo.inventory.iloc[1].filepath


def test_map_mask(eodatareaders_file, eodatareaders_params):
    """

    """

    S2_filepath, mask_filepath = create_mask(eodatareaders_file, eodatareaders_params)

    # Remove filter_bands and crop from params (done when creting mask)
    eodatareaders_params = [eodatareaders_params[0]]

    process = {
        "process_id": "mask",
        "arguments": {
            "data": {"from_node": "node_1"},
            "mask": {"from_node": "node_2"},
            "replacement": 0
        }
    }
    process['wrapper_dimension'] = 'band'

    params = map_mask(process)
    eodatareaders_params.extend(params)
    eo = EODataProcessor([S2_filepath, mask_filepath], eodatareaders_params)
    assert eo.get_data(band='mask')[0,0] == 0
    assert eo.get_data(band='mask')[-1,-1] == 2567
