from typing import NamedTuple

__all__ = ("Characteristics",)


class Characteristics(NamedTuple):
    attack_power: int
    attack_loot: int
    npc_power: int
    npc_loot: int

    @staticmethod
    def from_database(row):
        if row is None:
            return None
        return Characteristics(
            attack_power=row[3], attack_loot=row[4], npc_power=row[5], npc_loot=row[6]
        )

    @staticmethod
    def get_instance(
        atk_power: int = 0, atk_loot: int = 0, npc_power: int = 0, npc_loot: int = 0
    ):
        return Characteristics(
            attack_power=atk_power,
            attack_loot=atk_loot,
            npc_power=npc_power,
            npc_loot=npc_loot,
        )
