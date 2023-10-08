from patterns.structural.front_controller.front_controller import Request, RequestController


def main():
    request_controller = RequestController()

    request = Request("Yandex: what is life?")
    request_controller.dispatch_request(request)

    request = Request("Google: what is life?")
    request_controller.dispatch_request(request)

    request = Request("Bing: what is life?")
    request_controller.dispatch_request(request)


if __name__ == "__main__":
    main()
