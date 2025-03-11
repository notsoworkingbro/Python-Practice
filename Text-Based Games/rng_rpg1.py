# use global variable inside a class but outside a function
class Unit:
    def __init__(self, name, health, mana, armor, attack, movement_speed, evasion, skill):
        self.name = name
        self.health = health
        self.mana = mana
        self.armor = armor
        self.attack = attack
        self.movement_speed = movement_speed
        self.evasion = evasion
        self.skill = skill

class hero:
    Unit("pawn",         *[50, 100, 2, 3, 3, 10, 
        {"Hut" : (0, 1), 
        "Tower" : (0, 1), 
        "Town Hall" : (0, 1)
        
        }]),

    Unit("knight",         *[75, 200, 4, 6, 6, 80, 
        {"Kick" : (3, 5), 
        "Impale" : (5, 6), 
        "Charge" : (7, 7)
        
        }]),

    Unit("paladin",         *[100, 300, 6, 9, 9, 50, 
        {"Smash" : (5, 10), 
        "Holy Light" : (20, 15), 
        "Divine Armor" : (5, 20)
        
        }]),

    Unit("Archangel",         *[300, 300, 60, 90, 90, 500, 
        {"Holy Rush" : (5, 30), 
        "Blessing Light" : (20, 35), 
        "Grace" : (5, 30)
        
        }]),

    Unit("Sentinel",         *[400, 400, 50, 60, 190, 700, 
        {"Imitate" : (5, 50), 
        "Beam" : (20, 55), 
        "Divine Departure" : (5, 50)
        
        }])
    
    @classmethod
    def get_table(cls):
        return [key for key, value in vars(cls).items() if not isinstance(value, classmethod) and not key.startswith("__")]