from patterns.behavioral.state.state import Student


def main():
    student = Student()

    for i in range(4):
        student.perform()
        student.change_activity()


if __name__ == "__main__":
    main()
