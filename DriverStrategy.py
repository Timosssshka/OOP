from abc import ABC, abstractmethod

class DriverStrategy(ABC):

    @abstractmethod
    def read(self):
        pass
      
    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def display(self):
        pass
