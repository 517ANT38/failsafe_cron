
from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar("T")

class DataReader(ABC,Generic[T]):
    
    @abstractmethod
    def read(self) -> T:
        pass