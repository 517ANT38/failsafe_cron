
import sys


def get_params():
    data = sys.argv[1]
    log = sys.argv[2] 
    redis = sys.argv[3]
    return {
        "data_folder":data,
        "log_folder": log,
        "redis":redis
    }