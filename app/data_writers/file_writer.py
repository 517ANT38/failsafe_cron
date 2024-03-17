


from app.data_writers.data_writer import DataWriter


class FileWriter(DataWriter[str]):
    _filename:str
    def __init__(self,filename:str):
        self._filename = filename
    
    def write(self, data: str) -> None:
        with open(self._filename,"a") as f:
            f.write(data)           