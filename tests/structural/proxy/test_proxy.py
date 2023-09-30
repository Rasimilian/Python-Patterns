from patterns.structural.proxy.proxy import ServerEndpoint, Proxy


def test_proxy(capsys):
    server_endpoint = ServerEndpoint()
    server_endpoint.request()
    out, err = capsys.readouterr()
    assert out == "Accessing the server endpoint...\n"

    proxy = Proxy(server_endpoint)
    proxy.request()
    out, err = capsys.readouterr()
    assert out == "Checking access...\nLogging the time of the request...\nAccessing the server endpoint...\n"
