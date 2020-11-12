from abc import ABC

class API(ABC):

    def __init__(self, api_key):
        self._api_key = api_key
