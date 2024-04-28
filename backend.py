import requests # this is a synchronous application

API_URL = "https://api.willofsteel.me"

class Route:
    def __init__(self, path, method):
        self.path = API_URL + path
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
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "API-Key": api_key
        }

    def get_player(self):
        route = Route("/player", "GET")
        response = requests.get(route.path, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        # handle error here. ONLY error here is 403 Access Forbidden
        # this status code is soon to be changed to 401 Access Forbidden so handle both of them the same way