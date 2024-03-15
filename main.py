

from threading import Thread, get_native_id
import time
from data_readers.file_reader import FileReader
from data_writers.file_writer import FileWriter
from locks.redlock import Redlock

class CommonResource:
    x:int

commRes = CommonResource()

# def run(rl:Redlock):
#     lock = rl.lock("app",1000)
#     if not lock:
#         return
#     commRes.x = 0
#     for _ in range(1,5):
#         print(get_native_id(), commRes.x)
#         commRes.x +=1
#         time.sleep(100)
#     rl.unlock(rl)
        
def run():
    commRes.x = 0
    for _ in range(1,5):
        print(get_native_id(), commRes.x)
        commRes.x +=1
        # time.sleep(100)

if __name__ == "__main__":
    Thread(target=run).start()
    Thread(target=run).start()
    Thread(target=run).start()
    