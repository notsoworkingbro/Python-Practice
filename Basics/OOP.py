class Parent():

    # Encapsulation
    def __init__(self):
        # __init__ >>> initial when program starts
        self.name = "me"

    def printEverything(*args, **kwargs):
        for (item, value) in kwargs.items():
            print(f"{item}: {value}")
        
        print(*args)