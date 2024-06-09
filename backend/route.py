__all__ = "Route"

API_URL = "https://api.willofsteel.me"


class Route:
    def __init__(self, path, method):
        self.path = API_URL + path
        self.method = method.upper()

    def __str__(self):
        return self.path

    def __repr__(self):
        return f"Route({self.method} {self.path})"

    def __eq__(self, other):
        return self.path == other.path and self.method == other.method

    def __hash__(self):
        return hash((self.path, self.method))
