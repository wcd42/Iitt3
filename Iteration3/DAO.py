from abc import ABC, abstractmethod

class DAO(ABC):

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass