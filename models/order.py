from typing import NamedTuple

__all__ = ("MarketOrder",)


class MarketOrder(NamedTuple):
    item_id: str
    order_type: str
    price: int
    amount: int

    @staticmethod
    def from_data(data: dict | None):
        if data is None:
            return None
        return MarketOrder(
            item_id=data["item_type"],
            order_type=data["order_type"],
            price=data["price"],
            amount=data["amount"],
        )
