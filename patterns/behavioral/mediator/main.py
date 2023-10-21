from patterns.behavioral.mediator.mediator import Controller, View, Model
from patterns.behavioral.mediator.mediator_example_2 import SimpleUser, Admin, ChatRoom


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.handle_signal("Button clicked")
    controller.handle_signal("Button pressed")

    print("\nAnother example:")
    room = ChatRoom()
    admin = Admin(room, "ADMIN")
    user1 = SimpleUser(room, "USER1")
    user2 = SimpleUser(room, "USER2")

    room.set_admin(admin)
    room.add_user(user1)
    room.add_user(user2)

    user1.send_message("Hello!")
    print("\t")

    user2.send_message("Hi!")
    print("\t")

    admin.send_message("Welcome!")


if __name__ == "__main__":
    main()
