from patterns.creational.pool.pool import ObjectPool


def test_pool():
    pool = ObjectPool(size=2)

    # New items will be created
    something1 = pool.get_item()
    something2 = pool.get_item()
    something3 = pool.get_item()
    something1.value = 1
    something2.value = 2
    something3.value = 3
    assert id(something1) != id(something2)
    assert id(something2) != id(something3)
    assert something1.value == 1
    assert something2.value == 2
    assert something3.value == 3

    pool.put_item(something1)
    pool.put_item(something2)
    assert pool.size() == 2

    new_something1 = pool.get_item()
    new_something2 = pool.get_item()
    assert id(something1) == id(new_something1)
    assert id(something2) == id(new_something2)
    assert not new_something1.value
    assert not new_something1.value
