from random import choice, randint
import time

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

    def atk(self, *opponents):
        for opponent in opponents:
            rnd = randint(0,1)
            if self.health < 0:
                return print(f"Unit Died")
            
            # high ms attack first
            if self.movement_speed > opponent.movement_speed:

                if rnd == 1:
                    self.cast(opponent)
                                   
                else:
                    reduc_atk = (self.attack / opponent.armor +2)
                    opponent.health -= self.attack - reduc_atk

                    print(f"{self.name} attacked {opponent.name} instead and dealt {self.attack} dmg.")
            else:

                if rnd == 1:
                    opponent.cast(self)
                    print("WOW")

                else:
                    
                # rework
                    reduc_atk = (opponent.attack / (self.armor + 2))
                    self.health -= opponent.attack - reduc_atk
                    print(f"{opponent.name} attacked {self.name} and dealt {opponent.attack} dmg.")
 
    def cast(self, opponent):

            chosen_skill = (choice(list(self.skill.keys())))
            a, b = self.skill[chosen_skill]
            # print(chosen_skill, a, b)

            self.mana -= a
            opponent.health -= b
            print(f"{self.name} attacked {opponent.name} using {chosen_skill} and dealt {b} dmg.\n{self.name} has {self.mana} mana left.\n{opponent.name} has {opponent.health} health left")
            

        # for opponent in opponents:
        #     ...

    # Custom string representation output
    def __str__(self):
        return f"Unit:{" " * (16)}{self.name}\n"\
               f"Health:{" " * (14)}{self.health}\n"\
               f"Armor:{" " * (15)}{self.armor}\n"\
               f"Attack:{" " * (14)}{self.attack}\n"\
               f"Movement Speed:{" " * (6)}{self.movement_speed}"

# unit_lib = [
#     Unit("Unit name",         *[health, mana, armor, attack, movement_speed, evasion, 
#         {"Skill name 1" : (mana, damage), 
#         "Skill name 2" : (mana, damage), 
#         "Skill name 2" : (mana, damage)}]),
# ]



unit_lib = [
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
]

oppressed = choice(unit_lib)

# oppressed.cast(*[unit_lib[2] for i in range(3)])


oppressed.atk(*[choice(unit_lib) for i in range(3)])

# oppressed.cast(*[choice(unit_lib) for i in range(3)])
# oppressed.atk(*[choice(unit_lib) for i in range(3)])


# print(oppressed)

# print(choice(list(oppressed.skill.keys())))

# x = choice(list(oppressed.skill.keys()))
# a, b = oppressed.skill[x]

# print(oppressed.skill[x])
# print(a, b)

# print(unit_lib[2][6].skill('Divine Armor'))
# print(choice(oppressed.skill))

# x, y = d2[choice(list(d2.keys()))]
# print(x, y)

# test, test2 = unit_lib[choice(oppressed.skill)]
# print(test)

