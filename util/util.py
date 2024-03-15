from collections import namedtuple
import os

ObjLock = namedtuple("ObjLock", ("validity", "resource", "key"))

def get_unique_id():
    return os.urandom(30)