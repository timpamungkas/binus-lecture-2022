import math

class Calculator:

    def __init__(self, a, b):
        if a < 0 or a > 1000 or b < 0 or b > 1000:
            raise Exception("Numbers must between 0-1000") 

        self.a = a
        self.b = b

    def addition(self):
        return (self.a + self.b)

    def subtraction(self):
        return (self.a - self.b)

    def multiplication(self):
        return (self.a * self.b)

    def division(self):
        if self.b == 0:
            print("Division by zero")

        return (self.a / self.b)
    
    def pow(self):
        return pow(self.a, self.b)
    
#    def log(self):
#        return math.log(self.a, self.b);