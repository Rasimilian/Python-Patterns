from patterns.behavioral.memento.memento import Project, Repository


def test_memento():
    project = Project("project1", 1000)
    repository = Repository(project)
    repository.backup()
    assert repository.get_project_state() == {'_name': 'project1', '_cost': 1000}

    project.add_expenses(500)
    project.change_project_name("project2")
    repository.backup()
    assert repository.get_project_state() == {'_name': 'project2', '_cost': 1500}

    project.add_expenses(300)
    project.change_project_name("project3")
    assert repository.get_project_state() == {'_name': 'project3', '_cost': 1800}

    repository.undo()
    assert repository.get_project_state() == {'_name': 'project2', '_cost': 1500}

    repository.undo()
    assert repository.get_project_state() == {'_name': 'project1', '_cost': 1000}
