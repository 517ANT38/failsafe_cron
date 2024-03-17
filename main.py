

import os
from apps.app_worker_file import AppWorkerFile




if __name__ == "__main__":
    filename = os.environ.get("FILE_NAME")
    connect_str = os.environ.get("CONNECT_STRING")
    if not filename or not connect_str:
        raise EnvironmentError("Paramas not specified")
    app = AppWorkerFile(filename,connect_str)
    app.run()