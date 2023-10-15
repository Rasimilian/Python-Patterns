from patterns.behavioral.interpreter.interpreter import OrExpression, AndExpression, TerminalExpression


def test_interpreter():
    apple = TerminalExpression("Apple juice")
    apple_snack = TerminalExpression("Peach juice")
    anything_made_from = OrExpression(apple, apple_snack)

    apple = TerminalExpression("Apple juice")
    apple_chips = TerminalExpression("Peach juice")
    everything_made_from = AndExpression(apple, apple_chips)

    assert anything_made_from.interpret("Apple")
    assert not everything_made_from.interpret("Apple")

    assert anything_made_from.interpret("Peach")
    assert not everything_made_from.interpret("Peach")

    assert not anything_made_from.interpret("Orange")
    assert everything_made_from.interpret("juice")
