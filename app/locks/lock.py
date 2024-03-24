from abc import ABC,abstractmethod
from collections import namedtuple

LockObj = namedtuple("Lock", ("resource", "token"))

class Lock(ABC):

    @abstractmethod
    def acquire(self,resource_name:str,ttl:float) -> LockObj:
        pass
    @abstractmethod
    def release(self,lock_obj:LockObj) -> None:
        pass