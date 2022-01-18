from tkinter import E
from unicodedata import name


class Employee:
    def __init__(self,name):
        self.name=name
        self.company="Google"
        
# **** SINGLE INHERITANCE EXAMPLE
class Programmer(Employee):
    def getDetails(self):
        print(f"The employee name is {self.name} and his company is {self.company}")


p=Programmer("sujal")
p.getDetails()

