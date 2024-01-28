from abc import ABC, abstractmethod


class BackendService(ABC):
    @abstractmethod
    def get_data_from_database(self):
        ...
