from patterns.creational.abstract_factory.team_factory import get_team_factory


def main():
    """
    An abstract factory creates two teams working at the backend department and the marketing department.
    """
    backend_development_team = get_team_factory("Backend")
    java_developer = backend_development_team.create_developer()
    backend_team_pm = backend_development_team.create_project_manager()
    technical_analyst = backend_development_team.create_analyst()
    java_developer.write_code()
    backend_team_pm.manage()
    technical_analyst.analyze()

    marketing_team = get_team_factory("Marketing")
    python_developer = marketing_team.create_developer()
    marketing_team_pm = marketing_team.create_project_manager()
    marketing_analyst = marketing_team.create_analyst()
    python_developer.write_code()
    marketing_team_pm.manage()
    marketing_analyst.analyze()


if __name__ == "__main__":
    main()
