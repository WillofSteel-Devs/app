from __future__ import annotations

from aiohttp import ClientSession
from backend import Route
from models import Player, Alliance, MarketOrder
from .exceptions import AccessForbidden, ValidationError

__all__ = ("API",)


class API:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def setup(self):
        self.session = ClientSession(
            headers={
                "User-Agent": "WillofSteel API Client/1.0",
                "Content-Type": "application/json",
                "API-Key": self.api_key,
            }
        )

    async def request(
        self, route: Route, *, query_params: dict = {}, json: dict = {}, **kwargs
    ):
        method = route.method
        url = route.url

        async with self.session.request(
            method, url, params=query_params, json=json, **kwargs
        ) as response:
            response = await response.json()
        if response.status_code == 403:
            raise AccessForbidden(response.status_code)
            # handle error here however you want to
            # error 403 & 401 are Access Forbidden
        elif response.status_code == 422:
            raise ValidationError(response.status_code, json)

        return response

    async def get_player(self) -> Player | None:
        route = Route("/player", "GET")
        response = await self.request(route)
        data = await response.json()
        player = Player.from_data(data)
        return player

    async def get_alliance(self) -> Alliance | None:
        route = Route("/alliance", "GET")
        response = await self.request(route)
        data = await response.json()
        alliance = Alliance.from_data(data)
        return alliance

    async def update_alliance_name(self, name: str):
        route = Route("/alliance", "POST")
        query_params = {"update_type": "name", "new_name": name}
        response = await self.request(route, query_params=query_params)
        return await response.json()

    async def update_alliance_user_limit(self, user_limit: int):
        route = Route("/alliance", "POST")
        query_params = {"update_type": "user_limit", "new_limit": user_limit}
        response = await self.request(route, query_params=query_params)
        return await response.json()

    async def recruit_troop(self, troop_type: str, amount: str, currency: str = "gold"):
        route = Route("/recruit", "POST")
        query_params = {
            "troop_type": troop_type,
            "amount": amount,
            "currency": currency,
        }  # will be moved to payload in the future - Neil
        response = await self.request(route, query_params=query_params)
        return await response.json()

    async def get_market_orders(self):
        route = Route("/market", "GET")
        response = await self.request(route)
        orders = [MarketOrder.from_data(order) for order in await response.json()]
        return orders
