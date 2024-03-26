class LockException(Exception):
    def __init__(self, msg:str,err=None) -> None:
        self.msg = msg
        self.err = err