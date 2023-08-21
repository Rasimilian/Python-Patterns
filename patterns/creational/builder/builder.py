from typing import TypeVar
from abc import ABC, abstractmethod


class Smartphone:
    """An object of interest"""

    def set_company(self, company: str):
        self.company = company

    def set_operating_system(self, operating_system: str):
        self.operating_system = operating_system

    def set_logo(self, logo: str):
        self.logo = logo

    def __repr__(self):
        return f"Smartphone's info: Company name: {self.company}, OS: {self.operating_system}, Logo: {self.logo}"


class SmartphoneBuilder(ABC):
    def create_smartphone(self) -> None:
        self._smartphone = Smartphone()

    @abstractmethod
    def build_company_name(self) -> None:
        pass

    @abstractmethod
    def build_os_name(self) -> None:
        pass

    @abstractmethod
    def build_logo(self) -> None:
        pass

    def get_smartphone(self) -> Smartphone:
        return self._smartphone


class IphoneBuilder(SmartphoneBuilder):
    """Concrete Builder class implementation"""

    def build_company_name(self) -> None:
        self._smartphone.set_company("Apple Inc.")

    def build_os_name(self) -> None:
        self._smartphone.set_operating_system("IOS")

    def build_logo(self) -> None:
        self._smartphone.set_logo("Half-Bitten Apple")


class RedmiBuilder(SmartphoneBuilder):
    """Concrete Builder class implementation"""

    def build_company_name(self) -> None:
        self._smartphone.set_company("Xiaomi Inc.")

    def build_os_name(self) -> None:
        self._smartphone.set_operating_system("Android")

    def build_logo(self) -> None:
        self._smartphone.set_logo("MI")


SmartphoneBuilder_ = TypeVar("SmartphoneBuilder_", bound=SmartphoneBuilder)


class Director:
    def set_builder(self, builder: SmartphoneBuilder_):
        self.builder = builder

    def build_smartphone(self) -> Smartphone:
        self.builder.create_smartphone()
        self.builder.build_company_name()
        self.builder.build_os_name()
        self.builder.build_logo()

        return self.builder.get_smartphone()
