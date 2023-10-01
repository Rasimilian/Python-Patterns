from typing import List, Dict


class Model:
    def __init__(self):
        self.dataset = {"x": [], "y": []}

    def update_dataset(self, time_list: List[float], temperature_list: List[float]):
        self.dataset["x"] += time_list
        self.dataset["y"] += temperature_list


class View:
    def show_update_dataset_button(self):
        pass

    def show_plot_dataset_button(self):
        pass

    @staticmethod
    def render(dataset: Dict[str, List[float]]):
        for x_vals, y_vals in zip(dataset["x"], dataset["y"]):
            print(f"Showing y(x) dependency: x={x_vals}, y={y_vals}")


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def on_update_dataset_button(self, time_list: List[float], temperature_list: List[float]):
        """Controller has a listener listening View's button clicks by a user and receiving data the user enters."""

        self.model.update_dataset(time_list, temperature_list)
        self.view.render(self.model.dataset)
        print("Dataset has been updated")

    def on_plot_dataset_button(self):
        """Controller has a listener listening View's button clicks by a user and receiving data the user enters."""

        self.view.render(self.model.dataset)
