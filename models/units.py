from enum import Enum
from typing import NamedTuple

import emote

__all__ = ["UnitType"]


class UnitProperties(NamedTuple):
    name: str
    emote: str
    attack: int
    defense: int


class UnitType(UnitProperties, Enum):
    INFANTRY = UnitProperties("Infantry", emote.INFANTRY, 30, 20)
    CAVALRY = UnitProperties("Cavalry", emote.CAVALRY, 50, 30)
    ARTILLERY = UnitProperties("Artillery", emote.ARTILLERY, 90, 30)
    ASSASSINS = UnitProperties("Assassins", emote.ASSASSINS, 150, 25)
    BOWMEN = UnitProperties("Bowmen", emote.BOWMEN, 10, 35)
    BIG_BOWMEN = UnitProperties("Big Bowmen", emote.BIG_BOWMEN, 15, 55)
    HEAVY_MEN = UnitProperties("Heavy Men", emote.HEAVY_MEN, 15, 85)
    KINGS_GUARDS = UnitProperties("King's Guards", emote.KINGS_GUARDS, 30, 155)
