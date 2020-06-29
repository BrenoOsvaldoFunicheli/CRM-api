from .patterns.FormatStrategy import *
from .patterns import FORMATS


class PipedriveClass:

    def __init__(self):
        self.url = ''
        self.endpoint = ''

    def _format_params(self, params):
        """
        :param params: Uma lista de parametros que especifica attr extras para requisição REST na API
        :return: None
        """

        # Formata o final dos parametros da URI com attr={}
        params_lst = [k + '={}' for k, v in params.items()]
        # monta um set com os valores
        values_lst = (v for k, v in params.items())
        # Realiza a separação dos parametros por &
        params = "&".join(params_lst)

        # faz a junção do endpoint  com / e possíveis parametro adicionais
        self.url = self.endpoint + '/?' + params
        self.url = self.url.format(*values_lst)

    def _format_url_with_params(self, params):
        if params is not None:
            self._format_params(params)
        else:
            self.url = self.endpoint

    def get_by_id(self, id=0, params=None, return_as='dict', **kwargs):
        aux = self.endpoint
        self.endpoint += "/" + str(id)
        self._format_url_with_params(params)
        result = self._client._get(self._client.BASE_URL + self.url, **kwargs)
        self.endpoint = aux
        return FORMATS.get(return_as).return_as(result)

    def get_all(self, return_as='dict', params=None, **kwargs):
        self._format_url_with_params(params)
        result = self._client._get(self._client.BASE_URL + self.url, **kwargs)
        return FORMATS.get(return_as).return_as(result)
