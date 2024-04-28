from enum import Enum
from typing import NamedTuple, Callable

import emote


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


def total_attack(units: dict[UnitType, int]):
    return sum(map(lambda unit_type: unit_type.attack * units[unit_type], units.keys()))


def total_defense(units: dict[UnitType, int]):
    return sum(map(lambda unit_type: unit_type.defense * units[unit_type], units.keys()))


def lost_units(power: int, units: dict[UnitType, int], unit_power: Callable[[UnitType], int]) -> dict[UnitType, int]:
    lost = {}
    remaining_power = power
    sorted_units = sorted(units.items(), key=lambda x: (unit_power(x[0]), list(UnitType).index(x[0])))

    for unit_type, unit_count in sorted_units:
        units_taken = min(unit_count, round(remaining_power / unit_power(unit_type)))
        remaining_power -= units_taken * unit_power(unit_type)
        lost[unit_type] = units_taken

    return lost
