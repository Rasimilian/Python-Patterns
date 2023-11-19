import random

from patterns.other.blackboard.blackboard import SimpleWorker, HardWorker, Blackboard, Controller


def test_blackboard():
    final_progress = 11
    final_contributors = ['SimpleWorker', 'SimpleWorker', 'SimpleWorker', 'HardWorker', 'SimpleWorker', 'SimpleWorker', 'SimpleWorker', 'SimpleWorker', 'SimpleWorker', 'HardWorker']

    random.seed(42)

    blackboard = Blackboard(10)
    blackboard.add_worker(SimpleWorker(blackboard))
    blackboard.add_worker(HardWorker(blackboard))

    controller = Controller(blackboard)
    contributors = controller.run()
    progress = blackboard.progress
    assert progress == final_progress
    assert contributors == final_contributors
