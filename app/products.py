from .pipedrive_class import PipedriveClass


class Products(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'products'

    def get_product(self, product_id, **kwargs):
        self.url = self.endpoint + '/{}'.format(product_id)
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)

    def get_all_products(self, **kwargs):
        self.url = self.endpoint
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)

    def get_product_by_name(self, **kwargs):
        self.url = self.endpoint + '/find'
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)

    def create_product(self, data, **kwargs):
        self.url = self.endpoint
        return self._client._post(self._client.BASE_URL + self.url, json=data, **kwargs)

    def update_product(self, product_id, data, **kwargs):
        self.url = self.endpoint + '/{}'.format(product_id)
        return self._client._put(self._client.BASE_URL + self.url, json=data, **kwargs)

    def delete_product(self, product_id, **kwargs):
        self.url = self.endpoint + '/{}'.format(product_id)
        return self._client._delete(self._client.BASE_URL + self.url, **kwargs)

    def get_product_deal(self, product_id, **kwargs):
        self.url = self.endpoint + '/{}/deals'.format(product_id)
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)

    def get_product_fields(self, **kwargs):
        self.url = 'productFields'
        return self._client._get(self._client.BASE_URL + self.url, **kwargs)
