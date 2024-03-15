

from threading import Thread, get_native_id
import time
from data_readers.file_reader import FileReader
from data_writers.file_writer import FileWriter
from locks.redlock import Redlock

class CommonResource:
    x:int

commRes = CommonResource()

def run(rl:Redlock):
    while True:
        lock = rl.lock("app",1)
        if not lock:
            continue
        commRes.x = 0
        # print(lock)
        for _ in range(1,5):
            print(get_native_id(), commRes.x)
            commRes.x +=1
            time.sleep(0.1)
        rl.unlock(lock)
        
# def run():
#     commRes.x = 0
#     for _ in range(1,5):
#         print(get_native_id(), commRes.x)
#         commRes.x +=1
#         # time.sleep(100)



if __name__ == "__main__":
    rl = Redlock("redis://localhost:6379",1)
    
    Thread(target=run,args=[rl]).start()
    Thread(target=run,args=[rl]).start()
    Thread(target=run,args=[rl]).start()
    