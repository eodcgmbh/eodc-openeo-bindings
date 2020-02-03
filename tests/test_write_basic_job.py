"""
This test checks the output of a basic job.
"""

import os
import re
import shutil
from collections import namedtuple

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic():
    os.environ['CSW_SERVER'] = 'https://csw.eodc.eu'
    test_folder = os.getcwd()

    evi_file = os.path.join(test_folder, 'process_graphs/evi.json')
    job_data = os.path.join(test_folder, 'basic_job')
    out_filepath = os.path.join(test_folder, "basic_job.py")

    output_format, output_folder = BasicJobWriter(evi_file, job_data, output_filepath=out_filepath).write_job()
    assert output_format == 'Gtiff'
    assert 'save' in output_folder

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    refNode = namedtuple('RefNode', 'name input_filepaths')
    ref_node = [
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
    actual_nodes = re.split(r'### .+ ###', out_content)[1:]

    assert len(actual_nodes) == 14
    for i, actual_node in enumerate(actual_nodes):
        node_parts = re.split(r'# [A-Za-z ]+', actual_node)
        actual_files = node_parts[1].split('\n')[1]
        actual_params = node_parts[2].replace('\n', '')
        evaluate_node = node_parts[3].replace('\n', '')

        if ref_node[i].input_filepaths:
            actual_paths = re.search(r'\[.*\]', actual_files).group()
            actual_paths = actual_paths[2:-2].split("', '")

            # Check number of input filepaths match
            assert len(actual_paths) == len(ref_node[i].input_filepaths)
            for ref_dep, actual_input_path in zip(ref_node[i].input_filepaths, actual_paths):
                actual_path_name = actual_input_path.split('/')[-2]
                # Check input path match the correct dependency nodes
                assert actual_path_name.startswith(ref_dep)

        # Only parent folder is checked, but no other parameters
        actual_params = actual_params.split('=')[-1].strip()
        actual_params = eval(actual_params)
        for key, value in actual_params[0].items():
            # Check parent node name
            if key == 'folder_name':
                assert value.split('/')[-2].startswith(ref_node[i].name)

        assert evaluate_node.startswith(ref_node[i].name)
        # Check eoDataReader command
        assert re.match(r'^.+ = eoDataReader\(filepaths, params\)', evaluate_node)

    os.remove(out_filepath)
    shutil.rmtree(job_data)
