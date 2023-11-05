from patterns.behavioral.template.template import Linux, Windows


def main():
    system = Linux()
    system.start()

    print("\n")

    system = Windows()
    system.start()


if __name__ == "__main__":
    main()
