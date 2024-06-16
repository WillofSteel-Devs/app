from __future__ import annotations

import requests
from .route import Route
from models import Player, Alliance, MarketOrder
from .exceptions import AccessForbidden, ValidationError

__all__ = ("API",)


class API:
    def __init__(self, api_key: str):
        self.headers = {
            "User-Agent": "WillofSteel API Client/1.0",
            "Content-Type": "application/json",
            "API-Key": api_key,
        }
        self.api_key = api_key

    def request(
        self, route: Route, *, query_params: dict = {}, json: dict = {}, **kwargs
    ):
        method = route.method
        url = route.url

        response = requests.request(
            method, url, params=query_params, json=json, headers=self.headers, **kwargs
        )

        if response.status_code == 403:
            raise AccessForbidden(response.status_code)
            # handle error here however you want to
            # error 403 & 401 are Access Forbidden
        elif response.status_code == 422:
            raise ValidationError(response.status_code, json)

        return response

    def verify_key(self):
        route = Route("/verify", "GET")
        try:
            self.request(route)
        except AccessForbidden:
            return False
        return True

    def get_player(self) -> Player | None:
        route = Route("/player", "GET")
        response = self.request(route)
        data = response.json()
        player = Player.from_data(data)
        return player

    def get_alliance(self) -> Alliance | None:
        route = Route("/alliance", "GET")
        response = self.request(route)
        data = response.json()
        alliance = Alliance.from_data(data)
        return alliance

    def update_alliance_name(self, name: str):
        route = Route("/alliance", "POST")
        query_params = {"update_type": "name", "new_name": name}
        response = self.request(route, query_params=query_params)
        return response.json()

    def update_alliance_user_limit(self, user_limit: int):
        route = Route("/alliance", "POST")
        query_params = {"update_type": "user_limit", "new_limit": user_limit}
        response = self.request(route, query_params=query_params)
        return response.json()

    def recruit_troop(self, troop_type: str, amount: str, currency: str = "gold"):
        route = Route("/recruit", "POST")
        query_params = {
            "troop": troop_type.lower(),
            "amount": amount,
            "currency": currency.lower(),
        }  # will be moved to payload in the future - Neil
        response = self.request(route, query_params=query_params)
        return response

    def get_market_orders(self):
        route = Route("/market", "GET")
        response = self.request(route)
        orders = [MarketOrder.from_data(order) for order in response.json()]
        return orders
