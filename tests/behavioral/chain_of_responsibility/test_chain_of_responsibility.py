from patterns.behavioral.chain_of_responsibility.chain_of_responsibility import \
    Assistant, Manager, SeniorManager, Priority


def test_chain_of_responsibility(capsys):
    assistant = Assistant(priority=Priority.INFO)
    manager = Manager(priority=Priority.WARNING)
    senior_manager = SeniorManager(priority=Priority.CRITICAL)
    assistant.set_next(manager).set_next(senior_manager)

    assistant.handle("Excellent", priority=Priority.INFO)
    out, err = capsys.readouterr()
    assert out == "Assistant handles the request: Excellent\n"
    assert assistant._next_handler == manager

    assistant.handle("Fine", priority=Priority.WARNING)
    out, err = capsys.readouterr()
    assert out == "Manager handles the request: Fine\n"
    assert assistant._next_handler._next_handler == senior_manager
    assert manager._next_handler == senior_manager

    assistant.handle("Awful", priority=Priority.CRITICAL)
    out, err = capsys.readouterr()
    assert out == "Senior manager handles the request: Awful\n"
    assert not assistant._next_handler._next_handler._next_handler
    assert not senior_manager._next_handler
