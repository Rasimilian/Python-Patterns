

class Russian:
    def __init__(self):
        self.main_lang = "Russian"

    def speak(self) -> None:
        print("Privet!")


class American:
    def __init__(self):
        self.main_lang = "English"

    def speak_english(self) -> None:
        print("Hello!")


class Chinese:
    def __init__(self):
        self.main_lang = "Chinese"

    def speak_chinese(self) -> None:
        print("Ni Hao!")
