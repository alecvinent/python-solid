from ..datasource import Datasource


class API(Datasource):
    def get_data(self):
        return 'Data from the API'
