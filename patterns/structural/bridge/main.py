from patterns.structural.bridge.bridge import Institute, Company, IdeaMaker, MoneyMaker


def main():
    idea_maker = IdeaMaker()
    money_maker = MoneyMaker()

    institute = Institute(idea_maker)
    institute.operate()
    institute = Institute(money_maker)
    institute.operate()

    company = Company(idea_maker)
    company.operate()
    company = Company(money_maker)
    company.operate()


if __name__ == "__main__":
    main()
