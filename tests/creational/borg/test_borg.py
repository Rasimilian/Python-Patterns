from patterns.creational.borg.borg import SubBorg, AnotherBorg


def test_borg():
    borg1 = SubBorg()
    borg2 = SubBorg()
    assert id(borg1) != id(borg2)
    assert borg1 is not borg2
    assert borg1.state == borg2.state

    borg1.state = "Borg1"
    borg2.state = "Borg2"
    borg3 = SubBorg()
    assert id(borg1) != id(borg2)
    assert id(borg1) != id(borg3)
    assert borg1 is not borg2
    assert borg1 is not borg3
    assert borg1.state == borg2.state
    assert borg1.state == borg3.state

    borg4 = SubBorg("Borg4")
    assert id(borg1) != id(borg2)
    assert id(borg1) != id(borg4)
    assert borg1 is not borg2
    assert borg1 is not borg4
    assert borg1.state == borg2.state
    assert borg1.state == borg4.state

    # Borg with another _shared_state not shared with 1-4 Borgs
    borg5 = AnotherBorg("Borg5")
    assert id(borg1) != id(borg5)
    assert borg1 is not borg5
    assert borg1.state != borg5.state
