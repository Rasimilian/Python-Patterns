from patterns.behavioral.chain_of_responsibility.chain_of_responsibility import \
    Assistant, Manager, SeniorManager, Priority


def main():
    assistant = Assistant(priority=Priority.INFO)
    manager = Manager(priority=Priority.WARNING)
    senior_manager = SeniorManager(priority=Priority.CRITICAL)
    assistant.set_next(manager).set_next(senior_manager)

    assistant.handle("Excellent", priority=Priority.INFO)
    assistant.handle("Fine", priority=Priority.WARNING)
    assistant.handle("Awful", priority=Priority.CRITICAL)


if __name__ == "__main__":
    main()
