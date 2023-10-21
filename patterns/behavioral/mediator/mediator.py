from __future__ import annotations


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def handle_signal(self, event: str):
        if event == "Button clicked":
            self.model.change_data()
            self.view.render()
        elif event == "Button pressed":
            self.model.clear_data()
            self.view.hide()


class Model:
    def change_data(self):
        print("Changing data")

    def clear_data(self):
        print("Clearing data")


class View:
    def render(self):
        print("Showing graph")

    def hide(self):
        print("Hiding graph")
