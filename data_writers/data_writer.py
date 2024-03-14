from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class DataWriter(Generic[T]):
    @abstractmethod
    def write(self,data:T) -> None:
        pass