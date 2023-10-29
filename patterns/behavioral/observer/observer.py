from __future__ import annotations

from typing import List
from abc import ABC, abstractmethod


class Channel(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass


class TelegramChannel(Channel):
    _state: str = None
    _subscribers: List[Observer] = []

    def attach(self, observer: Observer):
        self._subscribers.append(observer)

    def detach(self, observer: Observer):
        self._subscribers.remove(observer)

    def notify_subscribers(self):
        for sub in self._subscribers:
            sub.update(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: str):
        self._state = value
        self.notify_subscribers()


class Observer(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def update(self, channel: Channel):
        pass


class FreeSubscriber(Observer):
    def update(self, channel: Channel):
        print(f"Free sub {self.name} doesn't get a notification that the Channel is {channel.state} now")


class PremiumSubscriber(Observer):
    def update(self, channel: Channel):
        print(f"Premium sub {self.name} gets a notification that the Channel is {channel.state} now")
