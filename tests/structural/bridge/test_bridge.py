from patterns.structural.bridge.bridge import MoneyMaker, IdeaMaker, Company, Institute


def test_bridge(capsys):
    idea_maker = IdeaMaker()
    money_maker = MoneyMaker()

    institute = Institute(idea_maker)
    institute.operate()
    out, err = capsys.readouterr()
    assert out == "Institute is working now...\nMaking ideas...\n"
    assert institute.maker == idea_maker

    institute = Institute(money_maker)
    institute.operate()
    out, err = capsys.readouterr()
    assert out == "Institute is working now...\nMaking money...\n"
    assert institute.maker == money_maker

    company = Company(idea_maker)
    company.operate()
    out, err = capsys.readouterr()
    assert out == "Company is working now...\nMaking ideas...\n"
    assert company.maker == idea_maker

    company = Company(money_maker)
    company.operate()
    out, err = capsys.readouterr()
    assert out == "Company is working now...\nMaking money...\n"
    assert company.maker == money_maker
