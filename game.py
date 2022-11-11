from room import Room
from treasure import Treasure
from npc import Npc
import random
from os import system, name
from clear import Clear


class Game:
	"""An adventure game exploring a cave system"""

	def __init__(self) -> None:
		# make rooms for the house
		entrance = Room("Entrance", "Snaggle toothed stalagmites poke out at you from the depths of a dark cavernous pit. Warning you- no BEACONING you- to enter. This cave system is named after it's oddly shaped cooridors and menacing personality- The Dragon's Lair.")
		first_cavern = Room(
			"First Cavern", "Your eyes adjust to the sight of a brilliant underground kaleidoscope full of twisted turns and sharp rock. Beautiful, yet deadly if you take a wrong step.")
		the_belly = Room("The Belly", "A huge cavern, must be forty feet across. They call this \'The Belly\' because of the humid sulfur smell leaking through the rocks. Droplets glimmer in your flashlight as they fall to the cavern floor from the hanging stalactites.")
		the_chute = Room("The Chute", "A tight and slick corridor- almost more fitting for a slip-and-slide than spelunking. If you can make it through the steep grade in this tunnel, you might just be able to make it out.")
		claws = Room("Claws", "They call this chasm \'claws\' for the way the menacing stalagmites rise from the cavern floor- threatening to tear you apart with every step. Tread lightly through this cooridor")
		tail = Room("Tail", "A gradually narrowing cave that snakes it way through the mountain. No one knows where it ends because it becomes too small for travel. You better bail out into a side passage before you get pinched!")
		the_pit = Room("The Pit", "Now you're really done in for. This cave is at the very bottom of the whole system- making it the number one place for creepy crawlies to collect when they wander in. Did you bring a rope? Because you\'re going to need it...")
		jaws_of_doom = Room("Jaws of Doom", "Named after the aggressive stalagmite/stalactite formations that seem to swallow you, should you dare to enter. This cavern has an opening that looks towards the sky...but at 40 feet up, that's no way out.")
		landing_pad = Room("The Landing Pad", "This cavern is long and straight, with smooth walls that blend into the floor. Some say it was carved out by glaciel water flows...others believe it's the entrance to the underworld.")

		# connect the rooms
		entrance.add_exits([first_cavern])
		first_cavern.add_exits([entrance, the_belly])
		the_belly.add_exits([first_cavern, tail, the_chute])
		the_chute.add_exits([the_belly, claws])
		claws.add_exits([the_pit, jaws_of_doom, the_chute])
		tail.add_exits([the_belly, jaws_of_doom])
		the_pit.add_exits([claws, landing_pad])
		jaws_of_doom.add_exits([landing_pad, tail])
		landing_pad.add_exits([jaws_of_doom, the_pit])

		# treasure items
		golden_egg = Treasure(
			"a Golden Egg", "A truly marvelous ovular rock that shimmers like gold in the sunlight.")
		rusty_hammer = Treasure(
			"a Rusty Hammer", "Long forgotten, this tool was left by the first cave explorers.")
		undies = Treasure(
			"Underwear", "A remnant of a lover\'s first escapade within these hallowed stone halls.")
		pet_rock = Treasure(
			"a Pet Rock", "The water has worn facial features into this squishy stone barely larger than your palm. \nIf stepped on, will let out a faint squeak that some say resembles \"Hello\"...")
		ruby = Treasure("the Dragon\'s Ruby",
						"A massive, 5lb, pure Ruby. Many have searched for it, but not many have found it...Don\'t let Arnold know you have it!")

		#npc's#
		arnold = Npc("Arnold", "Scraggly and worn, Arnold is an old, cankerous gold miner who's spent most of his life searching for the mythical Dragon\'s Ruby that's said to be lost in these chasms...")
		spiders = Npc("Monstrously Large Spiders",
					  "Huge arachnids that thrive in the dark, humid halls of the Dragon\'s lair. You better hurry on before they know you're here!")

		self.rooms = [entrance, first_cavern, the_belly, the_chute,
					  claws, tail, the_pit, jaws_of_doom, landing_pad]
		self.treasure_rooms = [first_cavern, the_belly, the_chute,
							   claws, tail, the_pit, jaws_of_doom, landing_pad]
		self.treasure_items = [golden_egg, rusty_hammer, undies, pet_rock]
		self.characters = [arnold, spiders]
		self.backpack = []
		self.current_room = entrance
		self.clear = Clear()

	def input_positive_integer(self, prompt: str, warning: str, min: int, max: int) -> int:
		"""Will present <prompt> for input, will not return until input is a positive integer in the given (inclusive) range of min and max.  Will present <warning> if user inputs something invalid."""

		while True:
			try:
				answer = int(input(prompt))
			except ValueError:
				print(warning)
				continue
			if answer >= min and answer <= max:
				break
			else:
				print(warning)

		return answer

	def play(self):
		"""Explore the Dragon's cave, starting at the entrance."""

		#assign treasure to rooms#
		for treasure in self.treasure_items:
			random_room = random.choice(self.treasure_rooms)
			random_room.treasure.append(treasure)

		#assign npc's to rooms#
		for person in self.characters:
			random_room = random.choice(self.treasure_rooms)
			random_room.npc.append(person)

		self.clear.clear()
		print('Welcome to the Dragon\'s Lair Cavern Explorer!')
		#Begin Game Play#
		while True:

			# Tell user who's in the room
			if bool(self.current_room.npc) == True:
				dude = self.current_room.npc.pop(0)
				print(
					f'\nYou found {dude.name}! \n{dude.description}')

			# Tell user where they are
			print('')
			print(f'*** You are in {self.current_room.name}. ***')
			print('-----')
			print(f'{self.current_room.description}')
			print('')

			# Get user input
			choice = input(
				"Would you like to (e)xit this cavern, (i)nspect the current one, or (q)uit? ")

			if choice == 'e':
				print("")
				counter = 1
				for room in self.current_room.exits:
					print(f'{counter}) {room.name}')
					counter += 1

				choice = self.input_positive_integer(
					"What's your next move?: ", "Not a valid option", 1, len(self.current_room.exits))
				choice -= 1  # human -> computer number
				self.current_room = self.current_room.exits[choice]
				self.clear.clear()

			if choice == 'i':
				if bool(self.current_room.treasure) == False:
					print('\n-------')
					print('Nothing to find here- keep exploring!')
					print('-------')
					self.clear.sleep(1)

				else:
					current_treasure = self.current_room.treasure.pop(0)
					print('-------')
					print(f'\nYou found {current_treasure.item}! {current_treasure.script} \nGood job inspecting! '
						  'It\'s been added to your spelunking bag, Cave Explorer.')
					self.backpack.append(current_treasure)
					self.clear.sleep(7)
				self.clear.clear()

			if choice == 'q':
				print('\nLet\'s look at all the things you found:')
				self.clear.sleep(2)
				num = 1
				for x in self.backpack:
						print(f'{num}) {x.item}')
						num += 1
				print('-------\n')
				break
