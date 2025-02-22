class Parent():

    # Encapsulation
    def __init__(self):
        # __init__ >>> initial when program starts
        self.name = 'me'

    # Use for args and kwargs
    def printEverything(self, *args, **kwargs):

        for (item, value) in kwargs.items():
            print(f"{item}: {value}")
        
        print(*args)

class Child(Parent):

    def hambog(self):
        self.name = 'gay'
        print(self.name)



child = Child()
child.hambog()
# hi nak (args, non keyword arguments) --- shokoy = 'alessandro delumban', bading = 'alessandro', maniac = 'delumban' (keyword arguments)
child.printEverything('Hi', 'nak', shokoy = 'alessandro delumban', bading = 'alessandro', maniac = 'delumban')
