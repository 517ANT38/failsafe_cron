
from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
R = TypeVar("R")

class TransformData(Generic[T,R]):
    
    @abstractmethod
    def transfrom(self,data:T) -> R:
        pass