from typing import NamedTuple

__all__ = "MarketOrder"


class MarketOrder(NamedTuple):
    uuid: str
    user_id: int
    item_id: str
    order_type: str
    price: int
    amount: int
    fulfilled: int

    @staticmethod
    def from_database(row):
        if row is None:
            return None
        return MarketOrder(
            uuid=row[0],
            user_id=row[1],
            item_id=row[2],
            order_type=row[3],
            price=row[4],
            amount=row[5],
            fulfilled=row[6],
        )
