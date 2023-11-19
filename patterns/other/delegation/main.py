from patterns.other.delegation.delegation import Delegate, Delegator


def main():
    delegate = Delegate()
    delegate.do_something()
    print(delegate.field)

    delegator = Delegator(delegate)
    delegator.do_something()
    print(delegator.field)


if __name__ == "__main__":
    main()
