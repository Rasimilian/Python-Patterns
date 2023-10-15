from patterns.behavioral.interpreter.interpreter import OrExpression, AndExpression, TerminalExpression


def main():
    apple = TerminalExpression("Apple juice")
    apple_snack = TerminalExpression("Peach juice")
    anything_made_from = OrExpression(apple, apple_snack)

    apple = TerminalExpression("Apple juice")
    apple_chips = TerminalExpression("Peach juice")
    everything_made_from = AndExpression(apple, apple_chips)

    print(anything_made_from.interpret("Apple"))
    print(everything_made_from.interpret("Apple"))

    print(anything_made_from.interpret("Peach"))
    print(everything_made_from.interpret("Peach"))

    print(anything_made_from.interpret("Orange"))
    print(everything_made_from.interpret("juice"))


if __name__ == "__main__":
    main()
