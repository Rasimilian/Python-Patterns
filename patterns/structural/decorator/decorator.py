from abc import ABC, abstractmethod
from typing import TypeVar


class Message(ABC):
    @abstractmethod
    def show(self):
        pass


Message_ = TypeVar("Message_", bound=Message)


class OralMessage(Message):
    def show(self):
        print(f"Oral message.")


class TextMessage(Message):
    def show(self):
        print(f"Text message.")


class MessageDecorator(Message):
    def __init__(self, message: Message_):
        self._message = message

    def show(self):
        self._message.show()


class MessageDuplicator(MessageDecorator):
    def show(self):
        super().show()
        super().show()


class MessageAugmentator(MessageDecorator):
    def show(self):
        print("Message augmented: ")
        super().show()
