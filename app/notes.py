from .pipedrive_class import PipedriveClass


class Notes(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'notes'

    def create_note(self, data, **kwargs):
        self.url = self.endpoint + ''
        return self._client._post(self._client.BASE_URL + self.url, json=data, **kwargs)

    def update_note(self, note_id, data, **kwargs):
        self.url = self.endpoint + '/{}'.format(note_id)
        return self._client._put(self._client.BASE_URL + self.url, json=data, **kwargs)

    def delete_note(self, note_id, **kwargs):
        self.url = self.endpoint + '/{}'.format(note_id)
        return self._client._delete(self._client.BASE_URL + self.url, **kwargs)

    def get_note_fields(self, **kwargs):
        self.url = 'noteFields'
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)
