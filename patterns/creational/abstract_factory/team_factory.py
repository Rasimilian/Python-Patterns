from . import *
from patterns.creational.abstract_factory.developer import Developer, JavaDeveloper, PythonDeveloper
from patterns.creational.abstract_factory.analyst import Analyst, TechnicalAnalyst, MarketingAnalyst
from patterns.creational.abstract_factory.project_manager import ProjectManager, BackendTeamProjectManager, \
    MarketingTeamProjectManager


Developer_ = TypeVar("Developer_", bound=Developer)
ProjectManager_ = TypeVar("ProjectManager_", bound=ProjectManager)
Analyst_ = TypeVar("Analyst_", bound=Analyst)


class TeamFactory(ABC):
    @abstractmethod
    def create_developer(self) -> Developer_:
        pass

    @abstractmethod
    def create_project_manager(self) -> ProjectManager_:
        pass

    @abstractmethod
    def create_analyst(self) -> Analyst_:
        pass


TeamFactory_ = TypeVar("TeamFactory_", bound=TeamFactory)


class BackendDevelopmentTeamFactory(TeamFactory):
    def create_developer(self) -> JavaDeveloper:
        return JavaDeveloper()

    def create_project_manager(self) -> BackendTeamProjectManager:
        return BackendTeamProjectManager()

    def create_analyst(self) -> TechnicalAnalyst:
        return TechnicalAnalyst()


class MarketingTeamFactory(TeamFactory):
    def create_developer(self) -> PythonDeveloper:
        return PythonDeveloper()

    def create_project_manager(self) -> MarketingTeamProjectManager:
        return MarketingTeamProjectManager()

    def create_analyst(self) -> MarketingAnalyst:
        return MarketingAnalyst()


def get_team_factory(department: str) -> TeamFactory_:
    departments = {"Backend": BackendDevelopmentTeamFactory,
                   "Marketing": MarketingTeamFactory}
    if department not in departments:
        raise ValueError("Unknown department!")

    return departments[department]()
