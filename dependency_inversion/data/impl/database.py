from ..datasource import Datasource


class Database(Datasource):
    def get_data(self):
        return 'Data from the database'
