"""
This test checks the input file generation of a basic job.
"""

import os

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(apply_file, out_filepath_basic_apply,
               setup_ref_job_folder, backend_processes, S2_filepaths):

    BasicJobWriter().write_job(process_graph_json=apply_file, job_data='./basic_job',
                               process_defs=backend_processes, in_filepaths=S2_filepaths,
                               output_filepath=out_filepath_basic_apply)
    
    with open(out_filepath_basic_apply) as outfile:
        out_content = outfile.read()

    filepath_split = os.path.splitext(out_filepath_basic_apply)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()
    
    assert out_content == ref_content
