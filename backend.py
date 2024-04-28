import requests # this is a synchronous application

API_URL = "https://api.willofsteel.me"

class Route:
    def __init__(self, path, method):
        self.path = path
        self.method = method.upper()

    def __str__(self):
        return f"Route({self.method} {self.path})"

    def __repr__(self):
        return f"Route({self.method} {self.path})"

    def __eq__(self, other):
        return self.path == other.path and self.method == other.method

    def __hash__(self):
        return hash((self.path, self.method))

class API:
    def __init__(self):
        pass