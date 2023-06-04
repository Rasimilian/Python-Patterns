import pytest

from patterns.creational.abstract_factory.team_factory import *


@pytest.mark.parametrize("department, expected_factory, expected_developer, expected_analyst, expected_pm",
[
    ("Backend", BackendDevelopmentTeamFactory, JavaDeveloper, TechnicalAnalyst, BackendTeamProjectManager),
    ("Marketing", MarketingTeamFactory, PythonDeveloper, MarketingAnalyst, MarketingTeamProjectManager)
])
def test_factory(department: str,
                 expected_factory: Type[TeamFactory_],
                 expected_developer: Type[Developer_],
                 expected_analyst: Type[Analyst_],
                 expected_pm: Type[ProjectManager_]):
    team_factory = get_team_factory(department)
    developer = team_factory.create_developer()
    analyst = team_factory.create_analyst()
    pm = team_factory.create_project_manager()
    developer.write_code()
    analyst.analyze()
    pm.manage()
    assert isinstance(team_factory, TeamFactory)
    assert isinstance(team_factory, expected_factory)
    assert isinstance(developer, Developer)
    assert isinstance(developer, expected_developer)
    assert isinstance(analyst, Analyst)
    assert isinstance(analyst, expected_analyst)
    assert isinstance(pm, ProjectManager)
    assert isinstance(pm, '2')
