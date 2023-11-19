from patterns.other.catalog.catalog import Catalog


def test_catalog(capsys):
    catalog1 = Catalog("func1")
    catalog1.main_func()
    out, err = capsys.readouterr()
    assert out == "Executing func1\n"
    assert catalog1.param == "func1"

    catalog2 = Catalog("func2")
    catalog2.main_func()
    out, err = capsys.readouterr()
    assert out == "Executing func2\n"
    assert catalog2.param == "func2"
