from __future__ import annotations

from typing import List
from abc import ABC, abstractmethod


class Chat(ABC):
    @abstractmethod
    def set_admin(self, admin: Admin):
        pass

    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def send_message(self, sender: User, message: str):
        pass


class User(ABC):
    def __init__(self, chat: Chat, name: str):
        self.chat = chat
        self.name = name

    @abstractmethod
    def get_message(self, message: str):
        pass

    @abstractmethod
    def send_message(self, message: str):
        pass


class Admin(User):
    def get_message(self, message: str):
        print(f"Admin {self.name} is receiving the message: {message}")

    def send_message(self, message: str):
        print(f"Admin {self.name} is sending the message: {message}")
        self.chat.send_message(self, message)


class SimpleUser(User):
    def get_message(self, message: str):
        print(f"User {self.name} is receiving the message: {message}")

    def send_message(self, message: str):
        print(f"User {self.name} is sending the message: {message}")
        self.chat.send_message(self, message)


class ChatRoom(Chat):
    def __init__(self):
        self.admin: Admin = None
        self.users: List[User] = []

    def set_admin(self, admin: Admin):
        self.admin = admin

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, sender: User, message: str):
        for user in self.users:
            if user != sender:
                user.get_message(message)
        if self.admin != sender:
            self.admin.get_message(message)
