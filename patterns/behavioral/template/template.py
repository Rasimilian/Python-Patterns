from abc import ABC, abstractmethod


class OperatingSystem(ABC):
    def start(self):
        print("System is starting")
        self.greet()
        print("Programs are running")

    @abstractmethod
    def greet(self):
        pass


class Linux(OperatingSystem):
    def greet(self):
        print("Hello from Linux")


class Windows(OperatingSystem):
    def greet(self):
        print("Hello from Windows")
