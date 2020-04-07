from funcs import *
from classes import *
import os

#initializes start() and reads name and class
specs = start()

#defines player character (name, class, equip, location)
hero = Player(specs[0], specs[1], [], (0, 0))

#creating items - so far limited to unique items due to drop and pick up functionality - WILL FIX
#weapons
sword = Weapon('sword', 'it\'s sharp', 1, 10, 5, 0.7)

#armor
gambeson = Armor('gambeson', 'it\'s a type of padded armor, this one is quite thick', 2, 5, 2, 0.9)

#other
lantern = Item('lantern', 'it can be lit to illuminate dark places', 1, 3)

#creating rooms
hall = Room('hall', 'it\'s a large hall with animal trophies on the walls', [lantern])
bedroom = Room('bedroom', 'it looks quite wealthy; the bed is covered in expensive sheets', [sword])
kitchen = Room('kitchen', 'there\'s a large oven and a lot of kitchenware', [gambeson])
living_room = Room('living room', 'it seems warm and cozy', [])

#indexing rooms
rooms = {(0, 0): hall, (0, 1): bedroom, (1, 0): living_room, (1, 1): kitchen}

#clear output
os.system('cls')

#current location description and prompt
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
        
        #picking up items
        elif 'take' in command or 'grab' in command or 'pick up' in command:
            if 'all' in command or 'everything' in command:
                for i in range(len(items_in_room)):
                    hero.equip.append(items_in_room[i])
                items_in_room.clear()
            else:
                for i in range(len(items_in_room)): #this is here to make sure multiple items can be picked up at the same time
                    try:
                        for i in range(len(items_in_room)):
                            if (items_in_room[i].name) in command:
                                hero.equip.append(items_in_room[i])
                                items_in_room.remove(items_in_room[i])
                    except IndexError:
                        continue #index error doesn't matter here, the loop will run again to pick up the next item

        #dropping items - similar to picking up, maybe i can make it more DRY???
        elif 'drop' in command or 'discard' in command or 'throw away' in command:
            if 'all' in command or 'everything' in command:
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
                                print(items_in_room)
                                print(hero.equip)
                    except IndexError:
                        continue

    except KeyError:
        input("You can\'t go there! Press ENTER to try again.")
        hero.location = current
        continue