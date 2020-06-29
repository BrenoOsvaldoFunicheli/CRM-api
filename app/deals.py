from .pipedrive_class import PipedriveClass


class Deals(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = "deals"

    def get_deal(self, deal_id, **kwargs):
        url = self.endpoint + '/{}'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_deal(self, data, **kwargs):
        url = self.endpoint
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_deal(self, deal_id, data, **kwargs):
        url = self.endpoint + '/{}'.format(deal_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_deal(self, deal_id, **kwargs):
        url = self.endpoint + '/{}'.format(deal_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def duplicate_deal(self, deal_id, **kwargs):
        url = self.endpoint + '/{}/duplicate'.format(deal_id)
        return self._client._post(self._client.BASE_URL + url, **kwargs)

    def get_deal_details(self, deal_id, **kwargs):
        url = self.endpoint + '/{}'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_deals_by_name(self, **kwargs):
        url = self.endpoint + '/find'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_deal_followers(self, deal_id, **kwargs):
        url = self.endpoint + '/{}/followers'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_follower_to_deal(self, deal_id, user_id, **kwargs):
        url = self.endpoint + '/{}/followers'.format(deal_id)
        data = {
            'user_id': user_id
        }
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_follower_to_deal(self, deal_id, follower_id, **kwargs):
        url = self.endpoint + '/{}/followers/{}'.format(deal_id, follower_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_deal_participants(self, deal_id, **kwargs):
        url = self.endpoint + '/{}/participants'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_participants_to_deal(self, deal_id, person_id, **kwargs):
        url = self.endpoint + '/{}/participants'.format(deal_id)
        data = {
            'person_id': person_id
        }
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_participant_to_deal(self, deal_id, participant_id, **kwargs):
        url = self.endpoint + '/{}/participants/{}'.format(deal_id, participant_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_deal_activities(self, deal_id, **kwargs):
        url = self.endpoint + '/{}/activities'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_deal_mail_messages(self, deal_id, **kwargs):
        url = self.endpoint + '/{}/mailMessages'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_deal_products(self, deal_id, **kwargs):
        url = self.endpoint + '/{}/products'.format(deal_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_deal_fields(self, **kwargs):
        url = 'dealFields'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_product_to_deal(self, deal_id, data, **kwargs):
        url = self.endpoint + '/{}/products'.format(deal_id)
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)
