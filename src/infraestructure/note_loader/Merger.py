from io import TextIOWrapper
from os.path import isfile
class MergerModel:
    def __init__(self,filename:str):
        self.filename = self.checkFilename(filename)
        self.io:TextIOWrapper = None
    @staticmethod
    def checkFilename(filename:str):
        if isfile(filename):
            return True
        raise ValueError("not file found")
    def __enter__(self):
        self.io:TextIOWrapper = open(self.filename,'r')
    def __exit__(self, exc_type, exc_value, traceback):
        self.io.close()