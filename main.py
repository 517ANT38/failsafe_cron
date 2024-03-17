

import os
from app.starters.starter_worker_file import StarterWorkerFile




if __name__ == "__main__":
    filename = os.environ.get("FILE_NAME")
    connect_str = os.environ.get("CONNECT_STRING")
    if not filename or not connect_str:
        raise EnvironmentError("Paramas not specified")
    app = StarterWorkerFile(filename,connect_str)    
    app.run()