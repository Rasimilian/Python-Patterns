from . import *


class Analyst(ABC):
    @abstractmethod
    def analyze(self):
        pass


class TechnicalAnalyst(Analyst):
    def analyze(self):
        print("Technical analyst does analysis of technical decisions.")


class MarketingAnalyst(Analyst):
    def analyze(self):
        print("Marketing analyst does analysis of marketing decisions.")
