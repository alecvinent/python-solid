from abc import ABC, abstractmethod


class FaxDevice(ABC):
    @abstractmethod
    def fax(self, document):
        ...
