from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input):
        pass