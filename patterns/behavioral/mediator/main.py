from patterns.behavioral.mediator.mediator import Controller, View, Model


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.handle_signal("Button clicked")
    controller.handle_signal("Button pressed")


if __name__ == "__main__":
    main()
