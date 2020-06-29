from .pipedrive_class import PipedriveClass


class WebHooks(PipedriveClass):
    def __init__(self, client):
        super().__init__()
        self._client = client
        self.endpoint = 'webhooks'

    def get_hooks_subscription(self, **kwargs):
        url = self.endpoint
        return self._client._get(url, **kwargs)

    def create_hook_subscription(self, subscription_url, event_action, event_object, **kwargs):
        url = self.endpoint
        data = {
            'subscription_url':
                subscription_url,
            'event_action': event_action,
            'event_object': event_object
        }
        return self._client._post(url, json=data, **kwargs)

    def delete_hook_subscription(self, hook_id, **kwargs):
        url = self.endpoint + '/{}'.format(hook_id)
        return self._client._delete(url, **kwargs)
