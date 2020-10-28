from eodc_openeo_bindings.map_array_processes import *
from eodatareaders.eo_data_reader import EODataProcessor
from test_utils import create_mask


def test_map_mask(eodatareaders_file, eodatareaders_params):
    """

    """

    S2_filepath, mask_filepath = create_mask(eodatareaders_file,
                                             eodatareaders_params,
                                             mask_val=1000
                                             )

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
