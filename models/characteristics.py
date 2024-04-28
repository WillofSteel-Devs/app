from typing import NamedTuple

class Characteristics(NamedTuple):	
	atk_power: int
	atk_loot: int
	npc_power: int
	npc_loot: int
	
	@staticmethod
	def from_database(row):
		if row is None:
			return None
		return Characteristics(
			atk_power=row[3],
			atk_loot=row[4],
			npc_power=row[5],
			npc_loot=row[6]
		)
	
	@staticmethod
	def from_param(atk_power: int = 0, atk_loot: int = 0, npc_power: int = 0, npc_loot: int = 0):
		return Characteristics(
			atk_power=atk_power,
			atk_loot=atk_loot,
			npc_power=npc_power,
			npc_loot=npc_loot
		)