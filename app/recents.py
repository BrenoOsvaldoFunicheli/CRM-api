from .pipedrive_class import PipedriveClass


class Recents(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'recents'

    def get_recent_changes(self, **kwargs):
        self.url = self.endpoint
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)
