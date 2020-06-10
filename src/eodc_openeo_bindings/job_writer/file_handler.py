import os

class FileHandler:

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None

    def open(self):
        self.file = open(self.filepath, 'w+')
        return self.file

    def close(self):
        # Remove addtional empty line at end of file
        last_line_no = self.file.seek(0, os.SEEK_END)
        self.file.seek(last_line_no-1)
        self.file.truncate()
        self.file.close()

    def append(self, content):
        self.file.write(content)
        return self.file
