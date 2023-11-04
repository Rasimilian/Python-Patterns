from patterns.behavioral.strategy.strategy import Student, Sleep, Work, Study


def test_strategy(capsys):
    student = Student(Sleep())
    student.perform()
    out, err = capsys.readouterr()
    assert out == "Sleeping\n"
    assert isinstance(student._activity, Sleep)

    student = Student(Work())
    student.perform()
    out, err = capsys.readouterr()
    assert out == "Working\n"
    assert isinstance(student._activity, Work)

    student = Student(Study())
    student.perform()
    out, err = capsys.readouterr()
    assert out == "Studying\n"
    assert isinstance(student._activity, Study)
