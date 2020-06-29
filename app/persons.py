from .pipedrive_class import PipedriveClass


class Persons(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = "persons"

    def get_persons_by_name(self, **kwargs):
        self.url = self.endpoint + '/find'
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)

    def create_person(self, data, **kwargs):
        self.url = self.endpoint
        return self._client._post(self._client.BASE_URL + self.url, json=data, **kwargs)

    def update_person(self, person_id, data, **kwargs):
        self.url = self.endpoint + '/{}'.format(person_id)
        return self._client._put(self._client.BASE_URL + self.url, json=data, **kwargs)

    def delete_person(self, person_id, **kwargs):
        self.url = self.endpoint + '/{}'.format(person_id)
        return self._client._delete(self.url, **kwargs)

    def get_person_deals(self, person_id, **kwargs):
        self.url = self.endpoint + '/{}/deals'.format(person_id)
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)

    def get_person_fields(self, **kwargs):
        self.url = 'personFields'
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)
