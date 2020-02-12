from abc import ABC, abstractmethod
import nbformat as nbf


class FileHandler(ABC):

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def append(self, content: str):
        pass


class BasicFileHandler(FileHandler):

    def open(self):
        self.file = open(self.filepath, 'w+')
        return self.file

    def close(self):
        self.file.close()

    def append(self, content):
        self.file.write(content)
        return self.file


class JupyterNotebookFileHandler(FileHandler):

    def open(self):
        job = nbf.v4.new_notebook()  # Instantiate jupyter notebook
        job['metadata'] = self.get_nb_metadata()  # Set kernel
        return job

    def close(self):
        # Write data to file!
        nbf.write(self.file, self.filepath)

    def append(self, content: str):
        self.file['cells'].append(nbf.v4.new_code_cell(content))
        return self.file

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

