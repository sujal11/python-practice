class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    def squareRoot(self):
        print(f"The squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")

a=Calculator(5)
a.square()
a.squareRoot()
a.cube()


