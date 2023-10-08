from patterns.structural.front_controller.front_controller import Request, RequestController


def test_front_controller(capsys):
    request_controller = RequestController()

    request = Request("Yandex: what is life?")
    request_controller.dispatch_request(request)
    out, err = capsys.readouterr()
    assert out == "Displaying a page in Yandex style\n"

    request = Request("Google: what is life?")
    request_controller.dispatch_request(request)
    out, err = capsys.readouterr()
    assert out == "Displaying a page in Google style\n"

    request = Request("Bing: what is life?")
    request_controller.dispatch_request(request)
    out, err = capsys.readouterr()
    assert out == "No search engine found for the request: Bing: what is life?\n"
