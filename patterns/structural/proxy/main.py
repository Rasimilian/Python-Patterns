from patterns.structural.proxy.proxy import ServerEndpoint, Proxy


def main():
    server_endpoint = ServerEndpoint()
    server_endpoint.request()
    print("\t")

    proxy = Proxy(server_endpoint)
    proxy.request()


if __name__ == "__main__":
    main()
