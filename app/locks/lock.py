from abc import ABC,abstractmethod

from app.util.util import ObjLock

class Lock(ABC):

    @abstractmethod
    def lock(self,resorce:str,ttl:int) -> ObjLock|bool:
        pass
    @abstractmethod
    def unlock(self,resorce:ObjLock) -> None:
        pass