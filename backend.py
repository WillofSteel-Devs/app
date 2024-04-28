import requests # this is a synchronous application
from models import Player, Alliance

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

class API:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "API-Key": api_key
        }

    def request(self, route: Route, data: dict = None):
        response = requests.request(route.method, route.path, headers=self.headers, json=data)
        if response.status_code == 403:
            raise Exception("Access Forbidden")
            # handle error here however you want to
            # error 403 & 401 are Access Forbidden

        return response

    def get_player(self) -> Player:
        route = Route("/player", "GET")
        response = self.request(route)
        data = response.json()
        player = Player.from_data(data, None)
        return player
    
    def get_alliance(self) -> Alliance:
        route = Route("/alliance", "GET")
        response = self.request(route)
        data = response.json()
        alliance = Alliance.from_data(data)
        return alliance