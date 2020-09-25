"""
This test checks the input file generation of a basic job using a python UDF.
"""


import os

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic_python_udf(test_folder, out_filepath_basic, backend_processes, S2_filepaths):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_python.json')

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data='./output_udf_python',
                               process_defs=backend_processes, in_filepaths=S2_filepaths[:2], output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_udf_python_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_basic_r_udf(test_folder, out_filepath_basic, backend_processes, S2_filepaths):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_r.json')

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data='./output_udf_r',
                               process_defs=backend_processes, in_filepaths=S2_filepaths[:2], output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_udf_r_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content
