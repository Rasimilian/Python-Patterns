from patterns.behavioral.mediator.mediator import Controller, View, Model
from patterns.behavioral.mediator.mediator_example_2 import SimpleUser, Admin, ChatRoom


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


def test_mediator_another_example(capsys):
    room = ChatRoom()
    admin = Admin(room, "ADMIN")
    user1 = SimpleUser(room, "USER1")
    user2 = SimpleUser(room, "USER2")

    room.set_admin(admin)
    room.add_user(user1)
    room.add_user(user2)
    assert len(room.users) == 2

    user1.send_message("Hello!")
    out, err = capsys.readouterr()
    assert out == "User USER1 is sending the message: Hello!\nUser USER2 is receiving the message: Hello!\nAdmin ADMIN is receiving the message: Hello!\n"

    user2.send_message("Hi!")
    out, err = capsys.readouterr()
    assert out == "User USER2 is sending the message: Hi!\nUser USER1 is receiving the message: Hi!\nAdmin ADMIN is receiving the message: Hi!\n"

    admin.send_message("Welcome!")
    out, err = capsys.readouterr()
    assert out == "Admin ADMIN is sending the message: Welcome!\nUser USER1 is receiving the message: Welcome!\nUser USER2 is receiving the message: Welcome!\n"
