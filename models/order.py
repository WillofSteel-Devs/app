from typing import NamedTuple

__all__ = ("MarketOrder",)


class MarketOrder(NamedTuple):
    order_type: str
    price: int
    amount: int

    @staticmethod
    def from_database(row):
        if row is None:
            return None
        return MarketOrder(
            item_id=row[2],
            order_type=row[3],
            price=row[4],
            amount=row[5],
        )
