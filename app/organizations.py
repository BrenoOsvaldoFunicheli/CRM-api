from .pipedrive_class import PipedriveClass


class Organizations(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'organizations'

    def create_organization(self, data, **kwargs):
        url = self.endpoint
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_organization(self, organization_id, data, **kwargs):
        url = self.endpoint + '/{}'.format(organization_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_organization(self, organization_id, **kwargs):
        url = self.endpoint + '/{}'.format(organization_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_organization_fields(self, **kwargs):
        url = 'organizationFields'
        return self._client._get(self._client.BASE_URL + url, **kwargs)
