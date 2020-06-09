"""
This test checks the input file generation of a basic job using a python UDF.
"""


import os
import re

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic_python_udf(csw_server, test_folder, out_filepath_basic, backend_processes):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_python.json')
    job_data = os.path.join(test_folder, 'output_udf_python')

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'### .+ ###', out_content)[1:]
    assert len(actual_nodes) == 3
    # TODO add proper checks


def test_basic_r_udf(csw_server, test_folder, out_filepath_basic, backend_processes):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_r.json')
    job_data = os.path.join(test_folder, 'output_udf_r')

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'### .+ ###', out_content)[1:]
    assert len(actual_nodes) == 3
    # TODO add proper checks
