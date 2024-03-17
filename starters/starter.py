from abc import ABC, abstractmethod


class Starter(ABC):
    @abstractmethod
    def run(self)->None:
        pass
    