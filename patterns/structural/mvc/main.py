from patterns.structural.mvc.mvc import Model, View, Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.on_update_dataset_button([1, 2], [100, 100])
    controller.on_plot_dataset_button()


if __name__ == "__main__":
    main()
