from patterns.behavioral.strategy.strategy import Student, Work, Sleep, Study


def main():
    student = Student(Sleep())
    student.perform()

    student = Student(Work())
    student.perform()

    student = Student(Study())
    student.perform()


if __name__ == "__main__":
    main()
