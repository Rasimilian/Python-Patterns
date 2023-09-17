from patterns.structural.adapter.base_objects import Russian, American, Chinese
from patterns.structural.adapter.adapter_via_inheritance import MestizoInheritance, MestizoComposition, client_code
from patterns.structural.adapter.adapter_no_inheritance import Adapter


def test_adapter_via_inheritance():
    russian = Russian()
    mestizo = MestizoInheritance()
    assert mestizo.main_lang == russian.main_lang
    assert hasattr(mestizo, "speak")

    mestizo = MestizoComposition(American())
    assert mestizo.main_lang == russian.main_lang
    assert hasattr(mestizo, "speak")


def test_adapter_no_inheritance():
    russian = Russian()
    obj = Adapter(russian, say_something=russian.speak)
    assert "main_lang" in obj.original_dict()
    assert obj.original_dict()["main_lang"] == russian.main_lang
    assert obj.main_lang == russian.main_lang
    assert "nationality" in obj.__dict__
    assert "say_something" in obj.__dict__

    american = American()
    obj = Adapter(american, say_something=american.speak_english)
    assert "main_lang" in obj.original_dict()
    assert obj.original_dict()["main_lang"] == american.main_lang
    assert obj.main_lang == american.main_lang
    assert "nationality" in obj.__dict__
    assert "say_something" in obj.__dict__

    chinese = Chinese()
    obj = Adapter(chinese, say_something=chinese.speak_chinese)
    assert "main_lang" in obj.original_dict()
    assert obj.original_dict()["main_lang"] == chinese.main_lang
    assert obj.main_lang == chinese.main_lang
    assert "nationality" in obj.__dict__
    assert "say_something" in obj.__dict__
