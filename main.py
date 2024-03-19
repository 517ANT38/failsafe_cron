
import logging
from app.starters.starter_worker_file import StarterWorkerFile

if __name__ == "__main__":
    try:
        StarterWorkerFile("file.txt","redis://localhost:6379").run()    
    except Exception as e:
        logging.exception("App exception",e)