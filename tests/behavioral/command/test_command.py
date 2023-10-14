from patterns.behavioral.command.command import ShowGraphCommand, UpdateDataCommand, UndoCommand, Invoker


def test_command(capsys):
    invoker1 = Invoker(UpdateDataCommand())
    invoker1.on_do_button()
    out, err = capsys.readouterr()
    assert out == "Updating data\n"
    assert len(UndoCommand.history) == 1

    invoker2 = Invoker(ShowGraphCommand())
    invoker2.on_do_button()
    out, err = capsys.readouterr()
    assert out == "Showing a graph\n"
    assert len(UndoCommand.history) == 2

    invoker3 = Invoker(UndoCommand())
    invoker3.on_do_button()
    out, err = capsys.readouterr()
    assert out == "Clearing a graph\n"
    assert len(UndoCommand.history) == 1

    invoker4 = Invoker(UndoCommand())
    invoker4.on_do_button()
    out, err = capsys.readouterr()
    assert out == "Restoring data\n"
    assert len(UndoCommand.history) == 0
