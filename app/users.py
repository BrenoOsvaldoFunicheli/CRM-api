from .pipedrive_class import PipedriveClass


class Users(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = "users"

    def get_me(self, **kwargs):
        url = self.endpoint + '/me'
        return self._client._get(self._client.BASE_URL + url, **kwargs)
