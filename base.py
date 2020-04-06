from funcs import *
from classes import *

#initializes start() and reads name and class
specs = start()

#defines player character (name, class, equip, location)
hero = Player(specs[0], specs[1], [], (0, 0))

#creating items
#weapons
sword = Weapon('a sword', 'it\'s sharp', 1, 10, 5, 0.7)

#armor
gambeson = Armor('a gambeson', 'it\'s a type of padded armor, this one is quite thick', 2, 5, 2, 0.9)

#other
lantern = Item('a lantern', 'it can be lit to illuminate dark places', 1, 3)

#creating rooms
hall = Room('a hall', 'it\'s a large hall with animal trophies on the walls', [sword, lantern, gambeson])
bedroom = Room('a bedroom', 'it looks quite wealthy; the bed is covered in expensive sheets', [])
kitchen = Room('a kitchen', 'there\'s a large oven and a lot of kitchenware', [])
living_room = Room('a living room', 'it seems warm and cozy', [])

#indexing rooms
rooms = {(0, 0): hall, (0, 1): bedroom, (1, 0): living_room, (1, 1): kitchen}

#current location description and prompt
while True:
    try:
        print(f'You\'re in {rooms[hero.location].name}. {rooms[hero.location].description.capitalize()}.')
        if len(rooms[hero.location].items) > 0:
            print('You see', end = ' ')
            for i in range(len(rooms[hero.location].items)):
                print(rooms[hero.location].items[i].name, end = '')
                if i < (len(rooms[hero.location].items) - 2):
                    print(', ', end = '')
                elif i < (len(rooms[hero.location].items) - 1):
                    print(' and ', end = '')
                else:
                    print('.')

        command = input("What do you do? ")

        #defining movement
        if 'go' in command:
            
            current = hero.location
            if 'north' in command:
                hero.location = (hero.location[0], hero.location[1] + 1)
            if 'east' in command:
                hero.location = (hero.location[0] + 1, hero.location[1])
            if 'west' in command:
                hero.location = (hero.location[0] - 1, hero.location[1])
            if 'south' in command:
                hero.location = (hero.location[0], hero.location[1] - 1)
    except KeyError:
        print("You can\'t go there!")
        hero.location = current
        continue