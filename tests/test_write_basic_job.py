"""
This test checks the input file generation of a basic job.
"""

import os

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(csw_server, test_folder, evi_file, evi_ref_node, out_filepath_basic, backend_processes):
    job_data = os.path.join(test_folder, 'basic_job')

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()
    
    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    
    assert out_content == ref_content


def test_UC1_basic(csw_server, test_folder, uc1_file, out_filepath_basic):
    job_data = os.path.join(test_folder, 'basic_job')
    backend_processes = 'https://openeo.eodc.eu/v1.0/processes'
    
    BasicJobWriter().write_job(process_graph_json=uc1_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)
    
    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()
    
    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_UC1_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content
    
    
