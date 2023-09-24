from patterns.structural.decorator.decorator import TextMessage, \
    OralMessage, MessageDuplicator, MessageAugmentator


def main():
    text_msg = TextMessage()
    text_msg.show()

    oral_msg = OralMessage()
    oral_msg.show()

    print("\nDecorated 1:")
    msg_duplicator = MessageDuplicator(TextMessage())
    msg_duplicator.show()
    msg_duplicator = MessageDuplicator(OralMessage())
    msg_duplicator.show()

    print("\nDecorated 2:")
    msg_augmentator = MessageAugmentator(TextMessage())
    msg_augmentator.show()
    msg_augmentator = MessageAugmentator(OralMessage())
    msg_augmentator.show()


if __name__ == "__main__":
    main()
