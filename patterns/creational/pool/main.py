from patterns.creational.pool.pool import CostlyResource, ObjectPool


def main():
    pool = ObjectPool(size=2)

    # New items will be created
    something1 = pool.get_item()
    something2 = pool.get_item()
    something3 = pool.get_item()
    something1.value = 1
    something2.value = 2
    something3.value = 3
    print(f"1 item: Value: {something1.value}, ID: {id(something1)}")
    print(f"2 item: Value: {something2.value}, ID: {id(something2)}")
    print(f"3 item: Value: {something3.value}, ID: {id(something3)}")

    pool.put_item(something1)
    pool.put_item(something2)
    print(f"Pool size: {pool.size()}")

    something1 = pool.get_item()
    something2 = pool.get_item()
    print(f"Value: {something1.value}, ID: {id(something1)}")
    print(f"Value: {something2.value}, ID: {id(something2)}")


if __name__ == "__main__":
    main()
