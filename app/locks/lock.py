from abc import ABC,abstractmethod

from app.util.util import ObjLock

class Lock(ABC):

    @abstractmethod
    def acquire(self,resorce:str,ttl:int) -> ObjLock:
        pass
    @abstractmethod
    def release(self,resorce:ObjLock) -> None:
        pass