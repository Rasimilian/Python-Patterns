from patterns.behavioral.state.state import Student


def test_state(capsys):
    activities = ["Sleeping\n", "Working\n", "Studying\n", "Sleeping\n"]

    student = Student()

    for i in range(4):
        student.perform()
        out, err = capsys.readouterr()
        assert out == activities[i]
        student.change_activity()
