from dependency_inversion.data.impl.database import Database
from dependency_inversion.service.backend_service import BackendService


class BackendServiceImpl(BackendService):
    def __init__(self, datasource: Database):
        self.datasource = datasource

    def get_data_from_database(self):
        return self.datasource.get_data()
