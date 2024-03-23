import logging
import os
from app.exceptions.lock_exception import LockException
from app.starters.starter_worker_file import StarterWorkerFile

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG,filename="file_log.log",format=FORMAT)

if __name__ == "__main__":    
    try:
        StarterWorkerFile("file.txt","redis://localhost:6379").run()
        logging.info("process [%s] successful write to file",os.getpid())           
    except LockException as e:
        logging.error("process [%s] error write to file: %s",os.getpid(),e.msg)
    