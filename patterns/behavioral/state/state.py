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
    def __init__(self):
        self._activity: Activity = Sleep()

    def change_activity(self):
        if isinstance(self._activity, Sleep):
            self._activity = Work()
        elif isinstance(self._activity, Work):
            self._activity = Study()
        elif isinstance(self._activity, Study):
            self._activity = Sleep()

    def perform(self):
        self._activity.perform()
