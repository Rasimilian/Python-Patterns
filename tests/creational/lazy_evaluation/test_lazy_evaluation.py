from patterns.creational.lazy_evaluation.lazy_evaluation import President


def test_lazy_evaluation():
    mr_president = President("Chinese", "Beijing")
    assert mr_president.__dict__ == {'nationality': 'Chinese', 'location': 'Beijing', 'greetings_num': 0,
                                     'colleagues_num': 0, 'friends_num': 0, 'siblings_num': 0}

    mr_president.greeting()
    assert mr_president.__dict__["greetings_num"] == 1
    assert mr_president.__dict__['_cached_greeting'] == 'Ni Hao!'
    mr_president.greeting()
    assert mr_president.__dict__["greetings_num"] == 1
    assert mr_president.__dict__['_cached_greeting'] == 'Ni Hao!'

    mr_president.colleagues
    assert mr_president.__dict__["colleagues_num"] == 1
    assert mr_president.__dict__['_cached_colleagues'] == 'Lots of colleagues'
    mr_president.colleagues
    assert mr_president.__dict__["colleagues_num"] == 1
    assert mr_president.__dict__['_cached_colleagues'] == 'Lots of colleagues'

    mr_president.friends
    assert mr_president.__dict__["friends_num"] == 1
    assert mr_president.__dict__['friends'] == 'Lots of friends'
    mr_president.friends
    assert mr_president.__dict__["friends_num"] == 1
    assert mr_president.__dict__['friends'] == 'Lots of friends'

    mr_president.siblings
    assert mr_president.__dict__["siblings_num"] == 1
    assert mr_president.__dict__['siblings'] == 'Lots of siblings'
    mr_president.siblings
    assert mr_president.__dict__["siblings_num"] == 1
    assert mr_president.__dict__['siblings'] == 'Lots of siblings'
