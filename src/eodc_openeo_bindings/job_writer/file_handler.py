class FileHandler:

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None

    def open(self):
        self.file = open(self.filepath, 'w+')
        return self.file

    def close(self):
        self.file.close()

    def append(self, content):
        self.file.write(content)
        return self.file
