from patterns.structural.decorator.decorator import TextMessage, OralMessage, MessageAugmentator, \
    MessageDuplicator, Message, MessageDecorator


def test_decorator(capsys):
    text_msg = TextMessage()
    text_msg.show()
    out, err = capsys.readouterr()
    assert out == "Text message.\n"
    assert isinstance(text_msg, Message)

    oral_msg = OralMessage()
    oral_msg.show()
    out, err = capsys.readouterr()
    assert out == "Oral message.\n"
    assert isinstance(oral_msg, Message)

    msg_duplicator = MessageDuplicator(TextMessage())
    msg_duplicator.show()
    out, err = capsys.readouterr()
    assert out == "Text message.\nText message.\n"
    assert isinstance(msg_duplicator, MessageDecorator)
    assert isinstance(msg_duplicator, Message)

    msg_duplicator = MessageDuplicator(OralMessage())
    msg_duplicator.show()
    out, err = capsys.readouterr()
    assert out == "Oral message.\nOral message.\n"
    assert isinstance(msg_duplicator, MessageDecorator)
    assert isinstance(msg_duplicator, Message)

    msg_augmentator = MessageAugmentator(TextMessage())
    msg_augmentator.show()
    out, err = capsys.readouterr()
    assert out == "Message augmented: \nText message.\n"
    assert isinstance(msg_augmentator, MessageDecorator)
    assert isinstance(msg_augmentator, Message)

    msg_augmentator = MessageAugmentator(OralMessage())
    msg_augmentator.show()
    out, err = capsys.readouterr()
    assert out == "Message augmented: \nOral message.\n"
    assert isinstance(msg_augmentator, MessageDecorator)
    assert isinstance(msg_augmentator, Message)
