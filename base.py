greeting = 'Hello adventurer, welcome to the mysterious mansion.'
name = input('Enter your name: ')

class Room:
    def __init__(self, description, items):
        self.description = description
        self.items = items

hall = Room('Is smells rotten in here.', 'There is a sword laying on the ground.')