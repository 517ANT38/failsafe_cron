
import os


def get_env():
    data = os.environ("DATA_FOLDER")
    log = os.environ("LOG_FOLDER") 
    redis = os.environ("REDIS_CONNECT")
    if not data:
        raise EnvironmentError("not DATA_FOLDER")
    if not log:
        raise EnvironmentError("not LOG_FOLDER")
    if not redis:
        raise EnvironmentError("not REDIS_CONNECT")
    return {
        "data_folder":data,
        "log_folder": log,
        "redis":redis
    }