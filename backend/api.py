import requests
from backend import Route
from models import Player, Alliance

from typing import Dict


class API:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def request(
        self, route: Route, *, query_params: dict = None, json: dict = None, **kwargs
    ):
        method = route.method
        url = route.url

        headers: Dict[str, str] = {
            "User-Agent": "WillofSteel API Client/1.0",
            "Content-Type": "application/json",
            "API-Key": self.api_key,
        }

        response = requests.request(
            method, url, headers=headers, params=query_params, json=json, **kwargs
        )
        if response.status_code == 403:
            raise Exception("Access Forbidden")
            # handle error here however you want to
            # error 403 & 401 are Access Forbidden

        return response

    def get_player(self) -> Player:
        route = Route("/player", "GET")
        response = self.request(route)
        data = response.json()
        player = Player.from_data(data)
        return player

    def get_alliance(self) -> Alliance:
        route = Route("/alliance", "GET")
        response = self.request(route)
        data = response.json()
        alliance = Alliance.from_data(data)
        return alliance
