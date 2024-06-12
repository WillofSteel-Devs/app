API_URL = "https://api.willofsteel.me"

__all__ = ("Route",)


class Route:
    def __init__(self, path, method):
        self.url = API_URL + path
        self.path = path
        self.method = method.upper()

    def __str__(self):
        return self.url

    def __repr__(self):
        return f"Route({self.method} {self.path})"

    def __eq__(self, other):
        return self.url == other.url and self.method == other.method

    def __hash__(self):
        return hash((self.url, self.method))
