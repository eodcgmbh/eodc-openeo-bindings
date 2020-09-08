"""
This test checks the input file generation of a basic job using a python UDF.
"""


import os

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic_python_udf(test_folder, out_filepath_basic, backend_processes, mocker):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_python.json')
    job_data = os.path.join(test_folder, 'output_udf_python')

    csw_server_response = [
        '/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip',
        '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip',
    ]
    mocker.patch('eodc_openeo_bindings.map_cubes_processes.csw_query', return_value=csw_server_response)

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()
    out_content = out_content.replace(test_folder, '')

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_udf_python_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content


def test_basic_r_udf(test_folder, out_filepath_basic, backend_processes, mocker):
    evi_file = os.path.join(test_folder, 'process_graphs', 'udf_r.json')
    job_data = os.path.join(test_folder, 'output_udf_r')

    csw_server_response = [
        '/s2a_prd_msil1c/2018/06/08/S2A_MSIL1C_20180608T101021_N0206_R022_T32TPS_20180608T135059.zip',
        '/s2a_prd_msil1c/2018/06/11/S2A_MSIL1C_20180611T102021_N0206_R065_T32TPS_20180611T123241.zip',
    ]
    mocker.patch('eodc_openeo_bindings.map_cubes_processes.csw_query', return_value=csw_server_response)

    BasicJobWriter().write_job(process_graph_json=evi_file, job_data=job_data,
                               process_defs=backend_processes, output_filepath=out_filepath_basic)

    with open(out_filepath_basic) as outfile:
        out_content = outfile.read()
    out_content = out_content.replace(test_folder, '')

    filepath_split = os.path.splitext(out_filepath_basic)[0]
    filename = filepath_split.split(os.path.sep)[-1]
    ref_filepath = os.path.join(os.environ['REF_JOBS'], filename + '_udf_r_ref.py')
    with open(ref_filepath) as outfile:
        ref_content = outfile.read()

    assert out_content == ref_content
