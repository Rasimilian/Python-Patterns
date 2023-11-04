from abc import ABC, abstractmethod


class Activity(ABC):
    @abstractmethod
    def perform(self):
        pass


class Study(Activity):
    def perform(self):
        print("Studying")


class Work(Activity):
    def perform(self):
        print("Working")


class Sleep(Activity):
    def perform(self):
        print("Sleeping")


class Student:
    def __init__(self, activity: Activity):
        self._activity = activity

    def perform(self):
        self._activity.perform()
