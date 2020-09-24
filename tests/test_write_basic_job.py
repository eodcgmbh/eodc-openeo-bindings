"""
This test checks the input file generation of a basic job.
"""


import os
from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(test_folder, evi_file, out_filepath_basic,
               backend_processes, S2_filepaths, setup_ref_job_folder):

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data='./basic_job',
                               process_defs=backend_processes, in_filepaths=S2_filepaths, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_UC1_temporal_basic(ACube_filepaths, test_folder, uc1_temporal_file, out_filepath_basic, setup_ref_job_folder):

    backend_processes = 'https://openeo.eodc.eu/v1.0/processes'

    BasicJobWriter().write_job(process_graph_json=uc1_temporal_file, job_data='./basic_job',
                               process_defs=backend_processes, in_filepaths=ACube_filepaths, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_UC1_temporal_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_UC1_spectral_basic(ACube_filepaths, test_folder, uc1_spectral_file, out_filepath_basic, setup_ref_job_folder):

    backend_processes = 'https://openeo.eodc.eu/v1.0/processes'

    BasicJobWriter().write_job(process_graph_json=uc1_spectral_file, job_data='./basic_job',
                               process_defs=backend_processes, in_filepaths=ACube_filepaths, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_UC1_spectral_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content
