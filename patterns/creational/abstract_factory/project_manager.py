from . import *


class ProjectManager(ABC):
    @abstractmethod
    def manage(self):
        pass


class BackendTeamProjectManager(ProjectManager):
    def manage(self):
        print("Backend PM manages a group of Java developers.")


class MarketingTeamProjectManager(ProjectManager):
    def manage(self):
        print("Marketing PM manages a group of Python developers.")
