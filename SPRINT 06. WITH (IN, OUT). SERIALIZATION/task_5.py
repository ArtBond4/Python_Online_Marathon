import json
import pickle
from enum import Enum


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)
        
        
class SerializeManager:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype
        self.file = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()

    def serialize(self, my_file):
        if self.filetype.value == 1:
            self.file = open(self.filename, 'ab')
            pickle.dump(my_file, self.file)
        else:
            self.file = open(self.filename, 'a')
            json.dump(my_file, self.file)


class FileType(Enum):
    JSON = 0
    BYTE = 1



def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)
