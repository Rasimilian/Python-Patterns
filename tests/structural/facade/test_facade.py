from patterns.structural.facade.facade import Company, Director, Worker, Accountant


def test_facade(capsys):
    company = Company()
    company.start()
    out, err = capsys.readouterr()
    assert out == "Director is managing.\nWorker is working.\nAccountant is sharing money.\n"
    assert isinstance(company.director, Director)
    assert isinstance(company.worker, Worker)
    assert isinstance(company.accountant, Accountant)
