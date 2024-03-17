from abc import ABC,abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class DataWriter(ABC,Generic[T]):
    @abstractmethod
    def write(self,data:T) -> None:
        pass