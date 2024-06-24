from .units import UnitType
from typing import NamedTuple

class NPCResult(NamedTuple):
    won: bool
    attacker_lost_troops: dict[UnitType, int]
    npc_lost_troops: dict[UnitType]
    gold_loot: int
    ruby_loot: int
    food_loot: int
    token_loot: str
    iron_frames: int

    @staticmethod
    def from_api(response: dict | None):
        if response is None:
            return None
        print(response)
        return NPCResult(
            won=response["won"],
            attacker_lost_troops={
                UnitType.INFANTRY: response["attacker_lost_units"]["infantry"],
                UnitType.CAVALRY: response["attacker_lost_units"]["cavalry"],
                UnitType.ARTILLERY: response["attacker_lost_units"]["artillery"],
                UnitType.ASSASSINS: response["attacker_lost_units"]["assassins"],
                UnitType.BOWMEN: response["attacker_lost_units"]["bowmen"],
                UnitType.BIG_BOWMEN: response["attacker_lost_units"]["big_bowmen"],
                UnitType.HEAVY_MEN: response["attacker_lost_units"]["heavy_men"],
                UnitType.KINGS_GUARDS: response["attacker_lost_units"]["kings_guards"],
            },
            npc_lost_troops={
                UnitType.INFANTRY: response["npc_lost_units"]["infantry"],
                UnitType.CAVALRY: response["npc_lost_units"]["cavalry"],
                UnitType.ARTILLERY: response["npc_lost_units"]["artillery"],
                UnitType.ASSASSINS: response["npc_lost_units"]["assassins"],
                UnitType.BOWMEN: response["npc_lost_units"]["bowmen"],
                UnitType.BIG_BOWMEN: response["npc_lost_units"]["big_bowmen"],
                UnitType.HEAVY_MEN: response["npc_lost_units"]["heavy_men"],
                UnitType.KINGS_GUARDS: response["npc_lost_units"]["kings_guards"],
            },
            gold_loot=response["gold_loot"],
            ruby_loot=response["ruby_loot"],
            food_loot=response["food_loot"],
            token_loot=response["token_loot"],
            iron_frames=response["iron_frames"],
        )