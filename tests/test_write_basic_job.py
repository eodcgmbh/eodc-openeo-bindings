"""
This test checks the input file generation of a basic job.
"""


import os
from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(csw_server_default, test_folder, evi_file, out_filepath_basic, backend_processes, setup_ref_job_folder):
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
    out_content = out_content.replace(test_folder, '')

    assert out_content == ref_content


def test_UC1_temporal_basic(acube_csw_server_default, test_folder, uc1_temporal_file, out_filepath_basic, setup_ref_job_folder):
    job_data = os.path.join(test_folder, 'basic_job')
    backend_processes = 'https://openeo.eodc.eu/v1.0/processes'

    BasicJobWriter().write_job(process_graph_json=uc1_temporal_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()
    out_content = out_content.replace(test_folder, '')

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_UC1_temporal_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_UC1_spectral_basic(acube_csw_server_default, test_folder, uc1_spectral_file, out_filepath_basic, setup_ref_job_folder):
    job_data = os.path.join(test_folder, 'basic_job')
    backend_processes = 'https://openeo.eodc.eu/v1.0/processes'

    BasicJobWriter().write_job(process_graph_json=uc1_spectral_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()
    out_content = out_content.replace(test_folder, '')

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_UC1_spectral_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content
