from abc import ABC, abstractmethod


class FrontendService(ABC):
    @abstractmethod
    def display_data(self):
        ...
