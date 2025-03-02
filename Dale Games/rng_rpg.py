class Enemies():

    def human(health, armor):
        health = 10
        armor = 10

    def __str__(self):
        return f"Enemy with {self.health} health and {self.armor} armor."

enemies = Enemies()
a = enemies.human()

print(a)

