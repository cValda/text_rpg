from funcs import *
from classes import *

#initializes start() and reads name and class
specs = start()

#defines player character
hero = Player(specs[0], specs[1], [], 0)

#creating rooms
hall = Room('You\'re in a large hallway.', 'There\'s nothing here.')
bedroom = Room('You\'re in a wealthy-looking bedroom.', 'There\'s nothing here.')
kitchen = Room('You\'re in the kitchen.', 'There\'s nothing here.')
living_room = ('You\'re in a comfortable living room.', 'There\'s nothing here.')


rooms = {(0, 0): hall, (0)}


while True:
    

