"""
This test checks the input file generation of a basic job using a python UDF.
"""


import os
import re

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic_python_udf(csw_server, test_folder):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_python.json')
    job_data = os.path.join(test_folder, 'output_udf_python')
    out_filepath = os.path.join(test_folder, "basic_udf_python.py")

    output_format, output_folder = BasicJobWriter(evi_file, job_data, output_filepath=out_filepath).write_job()
    assert output_format == 'Gtiff'
    assert 'udf' in output_folder

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'### .+ ###', out_content)[1:]
    assert len(actual_nodes) == 3

    os.remove(out_filepath)


def test_basic_r_udf(csw_server, test_folder):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_r.json')
    job_data = os.path.join(test_folder, 'output_udf_r')
    out_filepath = os.path.join(test_folder, "basic_udf_r.py")

    output_format, output_folder = BasicJobWriter(evi_file, job_data, output_filepath=out_filepath).write_job()
    assert output_format == 'Gtiff'
    assert 'udf' in output_folder

    with open(out_filepath) as outfile:
        out_content = outfile.read()

    actual_nodes = re.split(r'### .+ ###', out_content)[1:]
    assert len(actual_nodes) == 3

    os.remove(out_filepath)
