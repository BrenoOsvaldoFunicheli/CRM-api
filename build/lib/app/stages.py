from .pipedrive_class import PipedriveClass


class Stages(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'stages'

    def get_stages_by_pipeline(self, filter_id, **kwargs):
        url = self.endpoint + '?pipeline_id={}'.format(filter_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def create_stage(self, data, **kwargs):
        url = self.endpoint + ''
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_stage(self, stage_id, data, **kwargs):
        url = self.endpoint + '/{}'.format(stage_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_stage(self, stage_id, **kwargs):
        url = self.endpoint + '/{}'.format(stage_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def duplicate_stage(self, stage_id, **kwargs):
        url = self.endpoint + '/{}/duplicate'.format(stage_id)
        return self._client._post(self._client.BASE_URL + url, **kwargs)

    def get_stage_details(self, stage_id, **kwargs):
        url = self.endpoint + '/{}'.format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_stages_by_name(self, **kwargs):
        url = self.endpoint + '/find'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_stage_followers(self, stage_id, **kwargs):
        url = self.endpoint + '/{}/followers'.format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_follower_to_stage(self, stage_id, user_id, **kwargs):
        url = self.endpoint + '/{}/followers'.format(stage_id)
        data = {
            'user_id': user_id
        }
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_follower_to_stage(self, stage_id, follower_id, **kwargs):
        url = self.endpoint + '/{}/followers/{}'.format(stage_id, follower_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_stage_participants(self, stage_id, **kwargs):
        url = self.endpoint + '/{}/participants'.format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_participants_to_stage(self, stage_id, person_id, **kwargs):
        url = self.endpoint + '/{}/participants'.format(stage_id)
        data = {
            'person_id': person_id
        }
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_participant_to_stage(self, stage_id, participant_id, **kwargs):
        url = self.endpoint + '/{}/participants/{}'.format(stage_id, participant_id)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def get_stage_activities(self, stage_id, **kwargs):
        url = self.endpoint + '/{}/activities'.format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_stage_mail_messages(self, stage_id, **kwargs):
        url = self.endpoint + '/{}/mailMessages'.format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_stage_products(self, stage_id, **kwargs):
        url = self.endpoint + '/{}/products'.format(stage_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_stage_fields(self, **kwargs):
        url = 'stageFields'
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def add_product_to_stage(self, stage_id, data, **kwargs):
        url = self.endpoint + '/{}/products'.format(stage_id)
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)
