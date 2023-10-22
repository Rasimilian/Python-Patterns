from patterns.behavioral.memento.memento import Project, Repository


def main():
    project = Project("project1", 1000)
    repository = Repository(project)
    repository.backup()
    print(repository.get_project_state())

    project.add_expenses(500)
    project.change_project_name("project2")
    repository.backup()
    print(repository.get_project_state())

    project.add_expenses(300)
    project.change_project_name("project3")
    print(repository.get_project_state())

    repository.undo()
    print(repository.get_project_state())

    repository.undo()
    print(repository.get_project_state())


if __name__ == "__main__":
    main()
