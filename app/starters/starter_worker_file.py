
from app.starters.starter import Starter
from app.data_readers.file_reader import FileReader
from app.data_transform.transform_string import TransformStr
from app.data_writers.file_writer import FileWriter
from app.locks.redlock import Redlock


class StarterWorkerFile(Starter):
    def __init__(self,filename:str,redis_url:str):
        self.filename = filename
        self.data_reader = FileReader(filename)
        self.data_writer = FileWriter(filename)
        self.data_transform = TransformStr()
        self.red_lock = Redlock(redis_url)
        
    def run(self):                
        lock = self.red_lock.acquire(self.filename,1)
        s = self.data_reader.read()
        s = self.data_transform.transfrom(s)
        self.data_writer.write(s)
        self.red_lock.release(lock)
    