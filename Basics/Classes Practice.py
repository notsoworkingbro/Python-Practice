class Parent():

    # Encapsulation
    def __init__(self):
        # __init__ >>> initial when program starts
        self.name = 'parent'

    # Use for args and kwargs
    def printEverything(self, *args, **kwargs):

        for (item, value) in kwargs.items():
            print(f"{item}: {value}")
        
        print(*args)

class Child(Parent):
    # global name or variable
    global_name = "global_name"

    def __init__(self):
        # updates self
        super().__init__()
        self.name = "child"

    def print_name(self, *args, **kwargs):
        print(self.name)


    # no need for self reference
    @staticmethod
    def print_name(*args, **kwargs):
        # refers to the global name
        print(self.name)
    
    # requires self reference
    @classmethod
    def print_2(self, *args, **kwargs):
        print(self.name)

class Print:
    def printIt(self, *args, **kwargs):
        for (item, value) in kwargs.items():
            print(f"{item}: {value}")
        
        for x in args:
            print(f"{x}")

class Add:
    # global variables
    num1 = 1
    num2 = 2

    def __init__(self):
        # instances
        self.num1 = 3
        self.num2 = 4

    def get_sum_self(self):
        return self.num1 + self.num2
    
    @staticmethod
    # in static method there is no use for self
    def get_sum(num1, num2):
        print(num1 + num2)

    @classmethod
    # in class method must use cls instead of self
    def get_sum_class(cls, num3):
        print(cls.num1 + cls.num2 + num3)

add = Add()
p = Print()

for x in range(0, 4):
    # required parameters
    # using add variable to call staticmethod
    add.get_sum(x, x+3)

# can directly use class and call staticmethod however must need value on its parameters
Add.get_sum(1, 2)

# can directly use class and call classmethod, classmethod can use global variables but can also use other parameters
Add.get_sum_class(3)

child = Child()
# hi nak (args, non keyword arguments) --- name = 'alessandro delumban', fn = 'alessandro', ln = 'delumban' (keyword arguments)
child.printEverything('Hi', 'nak', name = 'alessandro delumban', fn = 'alessandro', ln = 'delumban')
