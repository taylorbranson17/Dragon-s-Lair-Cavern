class Room: 
	"""Represents a room in a house"""

	def __init__(self, name: str, description: str) -> None:
		self.name = name
		self.description = description
		self.exits = []
		self.treasure = []
		self.npc = []

	def add_exits(self, rooms: list):
		self.exits.extend(rooms)