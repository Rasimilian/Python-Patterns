from patterns.structural.mvc.mvc import Model, View, Controller


def test_mvc(capsys):
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.on_update_dataset_button([1, 2], [100, 100])
    controller.on_plot_dataset_button()
    out, err = capsys.readouterr()
    assert out == "Showing y(x) dependency: x=1, y=100\nShowing y(x) dependency: x=2, y=100\nDataset has been updated\nShowing y(x) dependency: x=1, y=100\nShowing y(x) dependency: x=2, y=100\n"
