from patterns.behavioral.observer.observer import TelegramChannel, FreeSubscriber, PremiumSubscriber


def main():
    channel = TelegramChannel()
    free_sub = FreeSubscriber("Alex")
    premium_sub = PremiumSubscriber("Jack")
    channel.attach(free_sub)
    channel.attach(premium_sub)

    channel.state = "Open"

    channel.detach(premium_sub)
    channel.state = "Closed"


if __name__ == "__main__":
    main()
