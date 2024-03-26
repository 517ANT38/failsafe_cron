import os
from app.exceptions.lock_exception import LockException
from app.log.util import get_logger
from app.starters.starter_worker_file import StarterWorkerFile
from app.util.util import get_env


if __name__ == "__main__":  
    
    envs = get_env() 
    logger = get_logger(envs["log_folder"]+"/log_app.log",__name__)
    try:
        StarterWorkerFile(envs["data_folder"]+"/app_data.txt",envs["redis"]).run()
        logger.info("successful write to file",pid=os.getpid())           
    except LockException as e:
        logger.error("error write file: %s",e.msg,pid=os.getpid())    