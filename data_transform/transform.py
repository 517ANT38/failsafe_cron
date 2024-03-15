
from abc import ABC,abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
R = TypeVar("R")

class TransformData(ABC,Generic[T,R]):
    
    @abstractmethod
    def transfrom(self,data:T) -> R:
        pass