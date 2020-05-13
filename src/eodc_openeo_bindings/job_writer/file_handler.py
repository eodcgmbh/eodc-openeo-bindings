from abc import ABC, abstractmethod


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
