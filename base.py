from funcs import *
from classes import *

#initializes start() and reads name and class
specs = start()

#defines player character
hero = Player(specs[0], specs[1], [], (0, 0))

#creating items
#weapons
sword = Weapon('a sharp sword', 1, 10, 5, 0.7)

#armor
gambeson = Armor('a thick gambeson', 2, 5, 2, 0.9)

#other
lantern = Item('a lantern that can be lit to illuminate dark places', 1, 3)

#creating rooms
hall = Room('You\'re in a large hallway.', [sword, lantern])
bedroom = Room('You\'re in a wealthy-looking bedroom.', 'There\'s nothing here.')
kitchen = Room('You\'re in the kitchen.', 'There\'s nothing here.')
living_room = Room('You\'re in a comfortable living room.', 'There\'s nothing here.')

#indexing rooms
rooms = {(0, 0): hall, (0, 1): bedroom, (1, 0): living_room, (1, 1): kitchen}

#current location description and prompt
while True:
    try:
        print(rooms[hero.location].description)
        command = input("What do you do? ")

        #defining movement
        if 'go' in command:
            current = hero.location
            if 'north' in command:
                hero.location = (hero.location[0], hero.location[1] + 1)
                print(hero.location)
            if 'east' in command:
                hero.location = (hero.location[0] + 1, hero.location[1])
                print(hero.location)
            if 'west' in command:
                hero.location = (hero.location[0] - 1, hero.location[1])
                print(hero.location)
            if 'south' in command:
                hero.location = (hero.location[0], hero.location[1] - 1)
                print(hero.location)
    except KeyError:
        print("You can\'t go there!")
        hero.location = current
        continue

