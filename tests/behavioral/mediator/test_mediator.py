from patterns.behavioral.mediator.mediator import Controller, View, Model


def test_mediator(capsys):
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.handle_signal("Button clicked")
    out, err = capsys.readouterr()
    assert out == "Changing data\nShowing graph\n"

    controller.handle_signal("Button pressed")
    out, err = capsys.readouterr()
    assert out == "Clearing data\nHiding graph\n"
