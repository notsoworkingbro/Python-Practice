# create Simple Calculator
# Later on create advanced Calculator
# can take many additions in 1 go

class PrintForMe:
    def printIt(self, *args, **kwargs):
        for (item, value) in kwargs.items():
            print(f"{Item} : {value}")

        for x in args:
            print(x)
        
class PEMDAS:
    def __init__(self):
        self.num1 = 10
        self.num2 = 2

    def add(self, num1, num2):
        return num1 + num2

    def minus(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1/num2

class Trigonometry:
    def sin(self, opp, hyp):
        return opp/hyp

    def cos(self, adj, hyp):
        return adj/hyp

    def tan(self, opp, adj, hyp):
        return (opp/hyp)/(adj/hyp)

class Areas:
    def circle(self, r):
        return (r*r)*3.14

    def square(self, l, w):
        return l*w

    def trinagle(self, b, h):
        return b*h/2

pp = PrintForMe()
operate = PEMDAS()

pp.printIt(operate.add(operate.num1, operate.num2))
pp.printIt(operate.minus(operate.num1, operate.num2))
pp.printIt(operate.multiply(operate.num1, operate.num2))
pp.printIt(operate.divide(operate.num1, operate.num2))

trig = Trigonometry()

pp.printIt(trig.sin(1, 1))
pp.printIt(trig.cos(1, 1))
pp.printIt(trig.tan(1, 1, 1))

area = Areas()

pp.printIt(area.circle(5))
pp.printIt(area.square(2, 5))
pp.printIt(area.trinagle(2, 4))

