from datetime import datetime
from typing import NamedTuple

from .units import UnitType
from .alliance import Alliance

class Player(NamedTuple):
    id: int
    registered_at: datetime
    gold: int
    ruby: int
    units: dict[UnitType, int]
    npc_level: int
    last_npc_win: datetime | None
    votes: int
    queue_slots: int
    alliance: Alliance
    silver: int
    observer: bool
    peace: int
    letter_bird: int
    food_stored: int
    prestige: int

    @staticmethod
    def from_database(row, alliance_data):
        if row is None:
            return None
        return Player(
            id=row[0],
            registered_at=row[1],
            gold=row[2],
            ruby=row[3],
            units={
                UnitType.INFANTRY: row[4],
                UnitType.CAVALRY: row[5],
                UnitType.ARTILLERY: row[6],
                UnitType.ASSASSINS: row[7],
                UnitType.BOWMEN: row[8],
                UnitType.BIG_BOWMEN: row[9],
                UnitType.HEAVY_MEN: row[10],
                UnitType.KINGS_GUARDS: row[11],
            },
            npc_level=row[12],
            last_npc_win=row[13],
            votes=row[14],
            alliance=alliance_data,
            queue_slots=row[16],
            silver=row[17],
            observer=True if row[18] == 1 else False,
            peace=row[19],
            letter_bird=True if row[20] == 1 else False,
            food_stored=row[21],
            prestige=row[22]
        )

class EventPlayer(NamedTuple):
    user_id: int
    event_points: int
    skins: list
    currently_wearing: int

    @staticmethod
    def from_database(row):
        if row is None:
            return None
        return EventPlayer(
            user_id=row[0],
            event_points=row[1],
            skins=row[2],
            currently_wearing=row[3]
        )