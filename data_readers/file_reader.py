from data_readers.data_read import DataReader


class FileReader(DataReader[str]):
    
    _filename:str
    
    def __init__(self,filename:str):
        self._filename = filename
    
    def read(self) -> str:
        with open(self._filename) as f:
            arr = f.readlines()
            if len(arr) == 0:
                return ""
            return arr[-1]