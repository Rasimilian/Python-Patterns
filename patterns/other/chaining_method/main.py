from patterns.other.chaining_method.chaining_method import Calculator


def main():
    calculator = Calculator()
    print(calculator.get_result())

    calculator.add(5).add(5).multiply(2)
    print(calculator.get_result())


if __name__ == "__main__":
    main()
