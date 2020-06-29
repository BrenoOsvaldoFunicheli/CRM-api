from .pipedrive_class import PipedriveClass


class Filters(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = "filters"

    def create_filter(self, data, **kwargs):
        self.url = self.endpoint
        return self._client._post(self._client.BASE_URL + self.url, json=data, **kwargs)

    def update_filter(self, filter_id, data, **kwargs):
        self.url = self.endpoint + '/{}'.format(filter_id)
        return self._client._put(self._client.BASE_URL + self.url, json=data, **kwargs)

    def delete_filter(self, filter_id, **kwargs):
        self.url = self.endpoint + '/{}'.format(filter_id)
        return self._client._delete(self._client.BASE_URL + self.url, **kwargs)
