import os
from app.exceptions.lock_exception import LockException
from app.log.util import get_logger
from app.starters.starter_worker_file import StarterWorkerFile
from app.util.util import get_params


if __name__ == "__main__":  
    
    params = get_params() 
    logger = get_logger(params["log_folder"]+"/cron.log",__name__)
    try:
        StarterWorkerFile(params["data_folder"]+"/app_data.txt",params["redis"]).run()
        logger.info("successful write to file",pid=os.getpid())           
    except LockException as e:
        logger.error("error write file: %s",e.msg,pid=os.getpid())    