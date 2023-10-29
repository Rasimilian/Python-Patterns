from patterns.behavioral.observer.observer import TelegramChannel, FreeSubscriber, PremiumSubscriber


def test_observer(capsys):
    channel = TelegramChannel()
    free_sub = FreeSubscriber("Alex")
    premium_sub = PremiumSubscriber("Jack")
    channel.attach(free_sub)
    channel.attach(premium_sub)

    channel.state = "Open"
    out, err = capsys.readouterr()
    assert out == "Free sub Alex doesn't get a notification that the Channel is Open now\nPremium sub Jack gets a notification that the Channel is Open now\n"

    channel.detach(premium_sub)
    channel.state = "Closed"
    out, err = capsys.readouterr()
    assert out == "Free sub Alex doesn't get a notification that the Channel is Closed now\n"
