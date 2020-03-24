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
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Weapon(Item):
    def __init__(self, damage, accuracy):
        self.damage = damage
        self.accuracy = accuracy

class Armor(Item):
    def __init__(self, protection, speed):
        self.protection = protection
        self.speed = speed