from abc import ABC, abstractmethod


class App(ABC):
    @abstractmethod
    def run(self)->None:
        pass
    