from patterns.structural.adapter.base_objects import Russian, American, Chinese
from patterns.structural.adapter.adapter_via_inheritance import MestizoInheritance, MestizoComposition, client_code
from patterns.structural.adapter.adapter_no_inheritance import Adapter


def main():
    russian = Russian()
    client_code(russian)
    mestizo = MestizoInheritance()
    client_code(mestizo)
    mestizo = MestizoComposition(American())
    client_code(mestizo)

    # Adapter via no inheritance
    print("\n")
    russian = Russian()
    obj = Adapter(russian, say_something=russian.speak)
    obj.say_something()
    print(obj.__dict__)
    print(obj.original_dict())
    print(obj.main_lang)
    print("\n")

    american = American()
    obj = Adapter(american, say_something=american.speak_english)
    obj.say_something()
    print(obj.__dict__)
    print(obj.original_dict())
    print(obj.main_lang)
    print("\n")

    chinese = Chinese()
    obj = Adapter(chinese, say_something=chinese.speak_chinese)
    obj.say_something()
    print(obj.__dict__)
    print(obj.original_dict())
    print(obj.main_lang)


if __name__ == "__main__":
    main()
