from __future__ import annotations

import requests
from backend import Route
from models import Player, Alliance, Order
from .exceptions import AccessForbidden, ValidationError
from typing import Dict

__all__ = ("API",)


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
            raise AccessForbidden(response.status_code)
            # handle error here however you want to
            # error 403 & 401 are Access Forbidden
        elif response.status_code == 422:
            raise ValidationError(response.status_code, json)

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
            "troop_type": troop_type,
            "amount": amount,
            "currency": currency,
        }  # will be moved to payload in the future - Neil
        response = self.request(route, query_params=query_params)
        return response.json()

    def get_market_orders(self):
        route = Route("/market", "GET")
        response = self.request(route)
        orders = [Order.from_data(order) for order in response.json()]
        return orders
