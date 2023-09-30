from abc import ABC, abstractmethod
from typing import TypeVar


class Endpoint(ABC):
    @abstractmethod
    def request(self):
        pass


Endpoint_ = TypeVar("Endpoint_", bound=Endpoint)


class ServerEndpoint(Endpoint):
    def request(self):
        print("Accessing the server endpoint...")


class Proxy(Endpoint):
    def __init__(self, endpoint: Endpoint_):
        self._endpoint = endpoint

    def check_access(self) -> bool:
        print("Checking access...")
        return True

    def log(self):
        print("Logging the time of the request...")

    def request(self):
        if self.check_access():
            self.log()
            self._endpoint.request()
