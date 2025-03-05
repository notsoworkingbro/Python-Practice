import random

class Unit:
    def __init__(self, name, health, armor, attack, movement_speed):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
        self.movement_speed = movement_speed

    # Custom string representation output
    def __str__(self):
        return f"|Unit: {self.name} |\n|Health: {self.health}|\n|Armor: {self.armor}|\n|Attack: {self.attack}|\n|Movement Speed: {self.movement_speed}|"

unit_lib = [
    ("pawn",         *[10, 2, 3, 3]),
    ("knight",         *[10, 2, 3, 3]),
    ("paladin",         *[10, 2, 3, 3])
]

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

