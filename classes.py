class Player:
    def __init__(self, name, clas, equip, location):
        self.name = name
        self.clas = clas
        self.equip = equip
        self.location = location
    def __repr__(self):
        return f'a {self.clas} called {self.name}'

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __repr__(self):
        return self.name

class Item:
    def __init__(self, name, description, weight, value):
        self.name = name
        self.description = description
        self.weight = weight
        self.value = value
    def __repr__(self):
        return self.name

class Weapon(Item):
    def __init__(self, name, description, weight, value, damage, accuracy):
        super().__init__(name, description, weight, value)
        self.damage = damage
        self.accuracy = accuracy
    def __repr__(self):
        return self.name
        

class Armor(Item):
    def __init__(self, name, description, weight, value, protection, speed):
        super().__init__(name, description, weight, value)
        self.protection = protection
        self.speed = speed
    def __repr__(self):
        return self.name