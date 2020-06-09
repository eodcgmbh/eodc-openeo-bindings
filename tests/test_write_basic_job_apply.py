"""
This test checks the input file generation of a basic job.
"""

import os
import re

from eodc_openeo_bindings.job_writer.basic_writer import BasicJobWriter


def test_basic(csw_server, test_folder, apply_file, out_filepath_basic_apply):
    job_data = os.path.join(test_folder, 'basic_job')

    BasicJobWriter().write_job(process_graph_json=apply_file, job_data=job_data,
                               output_filepath=out_filepath_basic_apply)
