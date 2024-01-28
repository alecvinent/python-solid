from abc import ABC, abstractmethod


class Datasource(ABC):
    @abstractmethod
    def get_data(self):
        ...
