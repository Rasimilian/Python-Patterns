import random

from patterns.other.blackboard.blackboard import SimpleWorker, HardWorker, Blackboard, Controller


def main():
    random.seed(42)

    blackboard = Blackboard(10)
    blackboard.add_worker(SimpleWorker(blackboard))
    blackboard.add_worker(HardWorker(blackboard))

    controller = Controller(blackboard)
    contributors = controller.run()
    print(blackboard.progress)
    print(contributors)


if __name__ == "__main__":
    main()
