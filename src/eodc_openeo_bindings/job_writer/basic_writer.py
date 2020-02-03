from eodc_openeo_bindings.job_writer.simple_job_writer import SimpleJobWriter


class BasicJobWriter(SimpleJobWriter):

    def get_default_filepath(self):
        return 'test.py'

    def open_job(self):
        return open(self.output_filepath, 'w+')

    def close_job(self, job):
        job.close()

    def append_to_job(self, job, content):
        job.write(content)
        return job
