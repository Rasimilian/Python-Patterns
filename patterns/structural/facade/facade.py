

class Director:
    def manage(self):
        print("Director is managing.")


class Worker:
    def work(self):
        print("Worker is working.")


class Accountant:
    def share_money(self):
        print("Accountant is sharing money.")


class Company:
    def __init__(self):
        self.director = Director()
        self.worker = Worker()
        self.accountant = Accountant()

    def start(self):
        self.director.manage()
        self.worker.work()
        self.accountant.share_money()
