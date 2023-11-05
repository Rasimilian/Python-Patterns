from __future__ import annotations

from abc import ABC, abstractmethod


class Organization(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

    @abstractmethod
    def work(self):
        pass


class Theatre(Organization):
    def accept(self, visitor: Visitor):
        visitor.visit_as_user(self)

    def work(self):
        print("Showing performance")


class Bank(Organization):
    def accept(self, visitor: Visitor):
        visitor.visit_as_worker(self)

    def work(self):
        print("Doing bank operations")


class Visitor(ABC):
    @abstractmethod
    def visit_as_worker(self, organization: Organization):
        pass

    @abstractmethod
    def visit_as_user(self, organization: Organization):
        pass


class Auditor(Visitor):
    def visit_as_worker(self, organization: Organization):
        organization.work()
        print("Auditor is executing an audit")

    def visit_as_user(self, organization: Organization):
        organization.work()
        print("Auditor is using services")


class Director(Visitor):
    def visit_as_worker(self, organization: Organization):
        organization.work()
        print("Director is managing the organization")

    def visit_as_user(self, organization: Organization):
        organization.work()
        print("Director is using services")
