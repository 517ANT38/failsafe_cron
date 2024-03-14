
from abc import abstractmethod
from typing import Generic, TypeVar


T = TypeVar("T")

class DataReader(Generic[T]):
    
    @abstractmethod
    def read(self) -> T:
        pass