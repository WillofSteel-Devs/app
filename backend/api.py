from __future__ import annotations

import requests
from .route import Route
from models import Player, Alliance, MarketOrder, UnitType, NPCResult
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
            print(response.json())
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
            "troop": troop_type.lower().replace(" ", "_").replace("'", ""),
            "amount": amount,
            "currency": currency.lower(),
        }  # will be moved to payload in the future - Neil

        response = self.request(route, query_params=query_params)
        return response

    def get_market_orders(self, item: str, order_type: str) -> list[MarketOrder | None]:
        route = Route("/market", "GET")
        query_params = {"item_type": item, "order_type": order_type}
        response = self.request(route, query_params=query_params)
        orders = response.json()["orders"]
        orders = [MarketOrder.from_data(order) for order in orders.values()]
        return orders

    def get_outposts(self):
        route = Route("/outpost/list", "GET")
        response = self.request(route)
        return response.json()

    def get_buildings(self):
        route = Route("/buildings", "GET")
        response = self.request(route)
        return response.json()

    def upgrade_building(self, building_type: str, levels_to_upgrade: str):
        route = Route("/buildings", "POST")

        query_params = {
            "building": building_type.lower(),
            "level": levels_to_upgrade,
        }

        response = self.request(route, query_params=query_params)
        return response.json()

    def attack_npc(self, troops: dict[UnitType, int]) -> NPCResult | None:
        route = Route("/npc", "POST")
        json = {"troops": troops}
        print(json)
        response = self.request(route, json=json)
        return NPCResult.from_api(response.json())
