from patterns.behavioral.command.command import Invoker, ShowGraphCommand, UpdateDataCommand, UndoCommand


def main():
    invoker1 = Invoker(UpdateDataCommand())
    invoker1.on_do_button()

    invoker2 = Invoker(ShowGraphCommand())
    invoker2.on_do_button()

    invoker3 = Invoker(UndoCommand())
    invoker3.on_do_button()

    invoker4 = Invoker(UndoCommand())
    invoker4.on_do_button()


if __name__ == "__main__":
    main()
