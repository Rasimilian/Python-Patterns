from patterns.behavioral.template.template import Linux, Windows


def test_template(capsys):
    system = Linux()
    system.start()
    out, err = capsys.readouterr()
    assert out == "System is starting\nHello from Linux\nPrograms are running\n"

    system = Windows()
    system.start()
    out, err = capsys.readouterr()
    assert out == "System is starting\nHello from Windows\nPrograms are running\n"
