"""
This test checks the input file generation of a basic job.
"""

import os

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(csw_server, test_folder, apply_file, out_filepath_basic_apply, setup_ref_job_folder, backend_processes):
    job_data = os.path.join(test_folder, 'basic_job')

    BasicJobWriter().write_job(process_graph_json=apply_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic_apply)
    
    with open(out_filepath_basic_apply) as outfile:
        out_content = outfile.read()
    
    filepath_split = os.path.splitext(out_filepath_basic_apply)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    
    assert out_content == ref_content
