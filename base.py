from funcs import *
from classes import *
import os

#defining commands
move = ['go', 'move', 'walk', 'run']
take = ['take', 'grab', 'pick up']
every = ['all', 'everything']
drop = ['drop', 'discard', 'throw away']
inventory = ['inventory', 'my items']

#creating items - it is now possible to have multiples of the same item
#weapons
sword = Weapon('sword', 'it\'s sharp', 1, 10, 5, 0.7)

#armor
gambeson = Armor('gambeson', 'it\'s a type of padded armor, this one is quite thick', 2, 5, 2, 0.9)

#other
lantern = Item('lantern', 'it can be lit to illuminate dark places', 1, 3)

#creating rooms
hall = Room('hall', 'it\'s a large hall with animal trophies on the walls', [lantern, sword])
bedroom = Room('bedroom', 'it looks quite wealthy; the bed is covered in expensive sheets', [sword])
kitchen = Room('kitchen', 'there\'s a large oven and a lot of kitchenware', [gambeson, sword])
living_room = Room('living room', 'it seems warm and cozy', [])

#indexing rooms
rooms = {(0, 0): hall, (0, 1): bedroom, (1, 0): living_room, (1, 1): kitchen}

#defines player character (name, class, equip, location)
specs = start()
hero = Player(specs[0], specs[1], [], (0, 0))

#clear output
os.system('cls')

#current location description
while True:
    os.system('cls')
    try:
        items_in_room = rooms[hero.location].items
        current_room_name = rooms[hero.location].name
        current_room_desc = rooms[hero.location].description
        print(f"You\'re in a {current_room_name}. {current_room_desc.capitalize()}.")
        if len(items_in_room) > 0:
            print("You see a ", end = '')
            for i in range(len(items_in_room)):
                print(items_in_room[i].name, end = '')
                if i < (len(items_in_room) - 2):
                    print(', a ', end = '')
                elif i < (len(items_in_room) - 1):
                    print(' and a ', end = '')
                else:
                    print('.')

#this section defines user commands
        command = input("What do you do? ")

        #defining movement
        if any(i in command for i in move):
            current = hero.location
            if 'north' in command:
                hero.location = (hero.location[0], hero.location[1] + 1)
            if 'east' in command:
                hero.location = (hero.location[0] + 1, hero.location[1])
            if 'west' in command:
                hero.location = (hero.location[0] - 1, hero.location[1])
            if 'south' in command:
                hero.location = (hero.location[0], hero.location[1] - 1)
        
        #picking up items
        elif any(i in command for i in take): #pick up
            if any(i in command for i in every): #everything
                for i in range(len(items_in_room)):
                    hero.equip.append(items_in_room[i])
                items_in_room.clear()
            else:
                duplicate_item = ''
                for i in range(len(items_in_room)): #this is here to make sure multiple items can be picked up at the same time
                    try:
                        for i in range(len(items_in_room)):
                            if items_in_room[i].name in command:
                                if items_in_room[i].name == duplicate_item:
                                    break
                                duplicate_item = items_in_room[i].name
                                hero.equip.append(items_in_room[i])
                                items_in_room.remove(items_in_room[i])
                    except IndexError:
                        continue

        #dropping items - similar to picking up, maybe i can make it more DRY???
        elif any(i in command for i in drop):
            if any(i in command for i in every):
                for i in range(len(hero.equip)):
                    items_in_room.append(hero.equip[i])
                hero.equip.clear()
            else:
                for i in range(len(hero.equip)):
                    try:
                        for i in range(len(hero.equip)):
                            if hero.equip[i].name in command:
                                items_in_room.append(hero.equip[i])
                                hero.equip.remove(hero.equip[i])
                    except IndexError:
                        continue
        elif any(i in command for i in inventory):
            if len(hero.equip) > 0:
                print("You have a ", end = '')
                for i in range(len(hero.equip)):
                    print(hero.equip[i].name, end = '')
                    if i < (len(hero.equip) - 2):
                        print(', a ', end = '')
                    elif i < (len(hero.equip) - 1):
                        print(' and a ', end = '')
                    else:
                        print('.')
                input('Press ENTER to continue.')
            else:
                print('You don\'t have anything, you poor bastard.')
                input('Press ENTER to continue.')

    except KeyError:
        input("You can\'t go there! Press ENTER to try again.")
        hero.location = current
        continue