from abc import ABC, abstractmethod


class ScannerDevice(ABC):
    @abstractmethod
    def scan(self, document):
        ...
