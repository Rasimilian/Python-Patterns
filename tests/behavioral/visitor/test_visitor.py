from patterns.behavioral.visitor.visitor import Theatre, Bank, Auditor, Director


def test_visitor(capsys):
    visitors = [Auditor(), Director()]

    theatre = Theatre()
    for visitor in visitors:
        theatre.accept(visitor)
    out, err = capsys.readouterr()
    assert out == "Showing performance\nAuditor is using services\nShowing performance\nDirector is using services\n"

    bank = Bank()
    for visitor in visitors:
        bank.accept(visitor)
    out, err = capsys.readouterr()
    assert out == "Doing bank operations\nAuditor is executing an audit\nDoing bank operations\nDirector is managing the organization\n"
