
from app.starters.starter_worker_file import StarterWorkerFile

if __name__ == "__main__":
    StarterWorkerFile("file.txt","redis://localhost:6379").run()    
    