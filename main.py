import os
from app.exceptions.lock_exception import LockException
from app.log.util import get_logger
from app.starters.starter_worker_file import StarterWorkerFile


logger = get_logger("file_log.log",__name__)
if __name__ == "__main__":    
    try:
        StarterWorkerFile("file.txt","redis://localhost:6379").run()
        logger.info("process [%s] successful write to file",os.getpid())           
    except LockException as e:
        logger.error("process [%s] error write to file: %s",os.getpid(),e.msg)
    