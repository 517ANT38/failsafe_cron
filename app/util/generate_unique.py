
from abc import ABC, abstractmethod


class GenerateUnique(ABC):
    @abstractmethod
    def generate(self,size:int)->str:
        pass