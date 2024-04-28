from datetime import datetime
from typing import NamedTuple


class Alliance(NamedTuple):
    owner: int
    created_at: datetime
    name: str
    user_limit: int
    bank: int

    @staticmethod
    def from_database(row):
        if row is None:
            return None
        
        return Alliance(
            owner = row[0],
            created_at=row[1],
            name=row[2],
            user_limit=row[3],
            bank=row[4]
        )