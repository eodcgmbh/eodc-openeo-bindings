"""
This test checks the input file generation of a basic job.
"""

import os
import re

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(csw_server, test_folder, evi_file, evi_ref_node, out_filepath_basic):
    job_data = os.path.join(test_folder, 'basic_job')

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data=job_data,
                               output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'### .+ ###', out_content)[1:]
    assert len(actual_nodes) == 14
    for i, actual_node in enumerate(actual_nodes):
        node_parts = re.split(r'# [A-Za-z ]+', actual_node)
        actual_files = node_parts[1].split('\n')[1]
        actual_params = node_parts[2].replace('\n', '')
        evaluate_node = node_parts[3].replace('\n', '')

        if evi_ref_node[i].input_filepaths:
            actual_paths = re.search(r'\[.*\]', actual_files).group()
            actual_paths = actual_paths[2:-2].split("', '")

            # Check number of input filepaths match
            assert len(actual_paths) == len(evi_ref_node[i].input_filepaths)
            for ref_dep, actual_input_path in zip(evi_ref_node[i].input_filepaths, actual_paths):
                actual_path_name = actual_input_path.split('/')[-2]
                # Check input path match the correct dependency nodes
                assert actual_path_name.startswith(ref_dep)

        # Only parent folder is checked, but no other parameters
        actual_params = actual_params.split('=')[-1].strip()
        actual_params = eval(actual_params)
        for key, value in actual_params[0].items():
            # Check parent node name
            if key == 'folder_name':
                assert value.split('/')[-2].startswith(evi_ref_node[i].name)

        assert evaluate_node.strip().startswith(evi_ref_node[i].name)
        # Check eoDataReader command
        assert re.match(r'^.+ = eoDataReader\(filepaths, params\)', evaluate_node)
