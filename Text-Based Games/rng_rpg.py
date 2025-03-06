from random import choice
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
            if self.health < 0:
                return print(f"Unit Died")
            
            # high ms attack first
            if self.movement_speed > opponent.movement_speed:
                reduc_atk = (self.attack / opponent.armor +2)
                opponent.health -= self.attack - reduc_atk

                return print(f"{self.name} attacked {opponent.name} instead and dealt {self.attack} dmg.")

            # rework
            reduc_atk = (opponent.attack / (self.armor + 2))
            self.health -= opponent.attack - reduc_atk
            print(f"{opponent.name} attacked {self.name} and dealt {opponent.attack} dmg.")
 
    def cast(self, *opponents):
        for opponent in opponents:
            print(opponent.skill[1])

        # for opponent in opponents:
        #     ...

    # Custom string representation output
    def __str__(self):
        return f"Unit:{" " * (16)}{self.name}\n"\
               f"Health:{" " * (14)}{self.health}\n"\
               f"Armor:{" " * (15)}{self.armor}\n"\
               f"Attack:{" " * (14)}{self.attack}\n"\
               f"Movement Speed:{" " * (6)}{self.movement_speed}"

unit_lib = [
    Unit("pawn",         *[10, 0, 2, 3, 3, 10, ["Hut", "Tower", "Town Hall"]]),
    Unit("knight",         *[15, 10, 4, 6, 6, 80, ["Kick", "Impale", "Charge"]]),
    Unit("paladin",         *[20, 30, 6, 9, 9, 50, ["Smash", "Holy Light", "Divine Armor"]])
]

oppressed = choice(unit_lib)
oppressed.atk(*[choice(unit_lib) for i in range(5)])

print(oppressed)

print(oppressed.skill)
# class Attack:
#     @staticmethod
#     def atk(suppressed, aggressor):
#         # If movement_speed1 > movement_speed2, pawn attacks knight
#         if suppressed.movement_speed > aggressor.movement_speed:
#             print('supressed flee')
#         else:
#             # dyanamic code for ARMOR HP / ATTACK REDUCTION
#             suppressed.health = suppressed.health - aggressor.attack + (suppressed.armor/10)
#             print(suppressed.health)

#         # Return the updated stats after the attack
#         return suppressed, aggressor

#     # mage stats coming soon
#     @staticmethod
#     def slow(pawn_stats, knight_stats):
#         ...

# class Spawn:
#     @staticmethod
#     def spawn1():
#         # Define the base stats and random unit selection
#         unit_lib = [
#             Unit("pawn",         *[10, 2, 3, 3]),
#             Unit("knight",       *[50, 10, 15, 10]),
#             Unit("paladdin",     *[50, 10, 15, 10])
#         ]
#         return unit_lib[random.randint(0, 2)]

#     @staticmethod
#     def spawn2():
#         # Define the base stats and random unit selection
#         unit_lib = [
#             Unit("king",         *[50, 10, 15, 10]),
#             Unit("archangel",    *[50, 10, 15, 10])
#         ]
#         return unit_lib[random.randint(0, 1)]

# spawned1 = Spawn.spawn1()
# spawned2 = Spawn.spawn2()

# Attack.atk(Spawn.spawn1(), Spawn.spawn2())

# Initialize the Human class and get stats
# print(pawn)

# Unit: pawn
# Health: 10
# Armor: 2
# Attack: 3
# Movement Speed: 3

# Attack.atk(pawn, knight)
# Attack.atk(pawn, knight)

# # Perform an attack
# updated_pawn_stats, updated_knight_stats = Attack.atk(pawn_stats, knight_stats)
# updated_pawn_stats, updated_knight_stats = Attack.atk(pawn_stats, knight_stats)
# updated_pawn_stats, updated_knight_stats = Attack.atk(pawn_stats, knight_stats)

# print("After the attack:")
# print("Updated Pawn Stats:", updated_pawn_stats)
# print("Updated Knight Stats:", updated_knight_stats)

