from patterns.other.delegation.delegation import Delegate, Delegator


def test_delegation(capsys):
    delegate = Delegate()
    delegate.do_something()
    print(delegate.field)
    out, err = capsys.readouterr()
    assert out == "Doing something\n99\n"

    delegator = Delegator(delegate)
    delegator.do_something()
    print(delegator.field)
    out, err = capsys.readouterr()
    assert out == "Doing something\n99\n"
