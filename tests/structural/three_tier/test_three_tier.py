from patterns.structural.three_tier.three_tier import UI


def test_three_tier(capsys):
    gui = UI()
    gui.show_objects()
    gui.show_object_by_id([1, 2])
    out, err = capsys.readouterr()
    assert out == "There is object1 in the system.\nThere is object2 in the system.\nThere is object3 in the system.\nThere is object1 with ID 1 in the system.\nThere is object2 with ID 2 in the system.\n"
