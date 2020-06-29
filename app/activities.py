# from numpy.testing._private.parameterized import param
from .pipedrive_class import PipedriveClass


class Activities(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'activities'

    def create_activity(self, data, **kwargs):
        self.url = self.endpoint
        return self._client._post(self._client.BASE_URL + self.url, json=data, **kwargs)

    def update_activity(self, activity_id, data, **kwargs):
        self.url = self.endpoint + '/{}'.format(activity_id)
        return self._client._put(self._client.BASE_URL + self.url, json=data, **kwargs)

    def delete_activity(self, activity_id, **kwargs):
        self.url = self.endpoint + '/{}'.format(activity_id)
        return self._client._delete(self._client.BASE_URL + self.url, **kwargs)

    def get_activity_fields(self, **kwargs):
        self.url = 'activityFields'
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)
