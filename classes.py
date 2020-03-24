class Player:
    def __init__(self, name, clas, equip, location):
        self.name = name
        self.clas = clas
        self.equip = equip
        self.location = location

class Room:
    def __init__(self, description, items):
        self.description = description
        self.items = items

class Item:
    def __init__(self, description, weight, value):
        self.description = description
        self.weight = weight
        self.value = value

class Weapon(Item):
    def __init__(self, description, weight, value, damage, accuracy):
        super().__init__(description, weight, value)
        self.damage = damage
        self.accuracy = accuracy

class Armor(Item):
    def __init__(self, description, weight, value, protection, speed):
        super().__init__(description, weight, value)
        self.protection = protection
        self.speed = speed