from abc import ABC, abstractmethod


class PrinterDevice(ABC):
    @abstractmethod
    def print(self, document):
        ...
