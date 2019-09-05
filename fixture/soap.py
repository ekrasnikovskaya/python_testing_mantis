from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        soap_config = self.app.config['soap']
        client = Client(soap_config['url'])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_info_from_soap(self):
        soap_config = self.app.config['soap']
        client = Client(soap_config['url'])
        info = client.service.mc_projects_get_user_accessible(soap_config['username'], soap_config['password'])
        array = []
        project_list = []
        for item in info:
            array.append(client.dict(item))
        for item in array:
            project_list.append(str(item['name']))
        return project_list




