import logging
from app.exceptions.lock_exception import LockException
from app.starters.starter_worker_file import StarterWorkerFile

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,filename="file_log.log")
    try:
        StarterWorkerFile("file.txt","redis://localhost:6379").run()            
    except LockException as e:
        logging.error("error write to file: %s",e.msg)
    