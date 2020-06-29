from .pipedrive_class import PipedriveClass


class Pipelines(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'pipelines'

    def get_pipeline_deals(self, pipeline_id, **kwargs):
        url = self.endpoint + '/{}/deals'.format(pipeline_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)
