

class YandexView:
    def show_content(self):
        print("Displaying a page in Yandex style")


class GoogleView:
    def show_content(self):
        print("Displaying a page in Google style")


class Request:
    SEARCH_ENGINES = ("Yandex", "Google")

    def __init__(self, request: str):
        self.request_text = request
        self.request_source = None
        if self.SEARCH_ENGINES[0] in request:
            self.request_source = self.SEARCH_ENGINES[0]
        elif self.SEARCH_ENGINES[1] in request:
            self.request_source = self.SEARCH_ENGINES[1]

    def __str__(self):
        return self.request_text


class Dispatcher:
    def __init__(self):
        self.yandex_view = YandexView()
        self.google_view = GoogleView()

    def dispatch(self, request: Request):
        if request.request_source == Request.SEARCH_ENGINES[0]:
            self.yandex_view.show_content()
        elif request.request_source == Request.SEARCH_ENGINES[1]:
            self.google_view.show_content()
        else:
            print(f"No search engine found for the request: {request}")


class RequestController:
    def __init__(self):
        self.dispatcher = Dispatcher()

    def dispatch_request(self, request: Request):
        self.dispatcher.dispatch(request)
