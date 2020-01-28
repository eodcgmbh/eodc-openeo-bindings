import nbformat as nbf

from eodc_openeo_bindings.job_writer.simple_job_writer import SimpleJobWriter


class JupyterNotebookWriter(SimpleJobWriter):

    def get_default_filepath(self) -> str:
        return 'test.ipynb'

    def open_job(self):
        job = nbf.v4.new_notebook()  # Instantiate jupyter notebook
        job['metadata'] = self.get_nb_metadata()  # Set kernel TODO : instead of = in original?
        return job

    def close_job(self, job):
        # Write data to file!
        nbf.write(job, self.filepath)

    def append_to_job(self, job, content):
        job['cells'].append(nbf.v4.new_code_cell(content))
        return job

    def get_nb_metadata(self):
        return {
            "kernelspec": {
                "display_name": "Python [conda env:eoDataReaders]",
                "language": "python",
                "name": "conda-env-eoDataReaders-py"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.7.3"
            }
        }
