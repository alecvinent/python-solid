from .backend_service_impl import BackendServiceImpl
from ..frontend_service import FrontendService


class FrontendServiceImpl(FrontendService):
    def __init__(self, backend: BackendServiceImpl):
        self.backend = backend

    def display_data(self):
        data = self.backend.get_data_from_database()
        print("Display data", data)
