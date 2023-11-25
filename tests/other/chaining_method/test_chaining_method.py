from patterns.other.chaining_method.chaining_method import Calculator


def test_chaining_method():
    calculator = Calculator()
    assert calculator.get_result() == 0

    calculator.add(5).add(5).multiply(2)
    assert calculator.get_result() == 20
