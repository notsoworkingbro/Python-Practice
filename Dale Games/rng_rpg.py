import random

# class Human():
#     @staticmethod
#     def pawn(health, armor, attack, movement_speed):
#         health = health
#         armor = armor
#         attack = attack
#         movement_speed = movement_speed

#         print(health, armor, attack, movement_speed)

#     @staticmethod
#     def knight(health, armor, attack, movement_speed):
#         health = health
#         armor = armor
#         attack = attack
#         movement_speed = movement_speed

#         print(health, armor, attack, movement_speed)

# class Attack():
#     @staticmethod
#     def atk(health1, armor1, attack1, movement_speed1, health2, armor2, attack2, movement_speed2):
#         if movement_speed1 > movement_speed2:
#             health2 = health2 - attack1
#         else:
#             health1 = health1 - attack2

# pawn_base_Stat = [10, 2, 3, 3]
# Knight_base_Stat = [50, 10, 15, 10]

# human = Human()
# human.pawn(*pawn_base_Stat)

class Human():
    @staticmethod
    def pawn(health, armor, attack, movement_speed):
        # Returns a dictionary for easier tracking of the stats
        return {
            'health': health,
            'armor': armor,
            'attack': attack,
            'movement_speed': movement_speed
        }

    @staticmethod
    def knight(health, armor, attack, movement_speed):
        return {
            'health': health,
            'armor': armor,
            'attack': attack,
            'movement_speed': movement_speed
        }

class Attack():
    @staticmethod
    def atk(pawn_stats, knight_stats):
        # If movement_speed1 > movement_speed2, pawn attacks knight
        if pawn_stats['movement_speed'] > knight_stats['movement_speed']:
            knight_stats['health'] -= pawn_stats['attack']
        else:
            pawn_stats['health'] -= knight_stats['attack']

        # Return the updated stats after the attack
        return pawn_stats, knight_stats



# Define the base stats
pawn_base_Stat = [10, 2, 3, 3]
Knight_base_Stat = [50, 10, 15, 10]

# Initialize the Human class and get stats

pawn_stats = Human.pawn(*pawn_base_Stat)
knight_stats = Human.knight(*Knight_base_Stat)

# Print the initial stats
print("Pawn Stats:", pawn_stats)
print("Knight Stats:", knight_stats)

# Perform an attack
updated_pawn_stats, updated_knight_stats = Attack.atk(pawn_stats, knight_stats)

updated_pawn_stats, updated_knight_stats = Attack.atk(pawn_stats, knight_stats)

updated_pawn_stats, updated_knight_stats = Attack.atk(pawn_stats, knight_stats)

print("After the attack:")
print("Updated Pawn Stats:", updated_pawn_stats)
print("Updated Knight Stats:", updated_knight_stats)

