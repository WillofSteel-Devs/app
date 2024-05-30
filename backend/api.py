import requests
from backend import Route
from models import Player, Alliance

class API:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "API-Key": api_key
        }

    def request(self, route: Route, data: dict = None) -> dict:
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
        print(data)
        player = Player.from_data(data, None)
        return player
    
    def get_alliance(self) -> Alliance:
        route = Route("/alliance", "GET")
        response = self.request(route)
        data = response.json()
        alliance = Alliance.from_data(data)
        return alliance