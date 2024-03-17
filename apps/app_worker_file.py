
from apps.app import App
from data_readers.file_reader import FileReader
from data_transform.transform_string import TransformStr
from data_writers.file_writer import FileWriter
from locks.redlock import Redlock


class AppWorkerFile(App):
    def __init__(self,filename:str,redis_url:str):
        self.resorce = filename
        self.data_reader = FileReader(filename)
        self.data_writer = FileWriter(filename)
        self.data_transform = TransformStr()
        self.red_lock = Redlock(redis_url)
    def run(self) -> None:
        lock = self.red_lock.lock(self.resorce,1)
        if not lock:
            return
        s = self.data_reader.read()
        s = self.data_transform.transfrom(s)
        self.data_writer.write(s)
        self.red_lock.unlock(lock)
        
    