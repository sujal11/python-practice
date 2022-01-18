class Employee:
    company="Google"
    def __init__(self,name):
        self.name=name
        

class Student:
    company="Youtube"        
        
# **** SINGLE INHERITANCE EXAMPLE
class Programmer(Employee,Student):
    def getDetails(self):
        print(f"The employee name is {self.name} and his company is {self.company}")


p=Programmer("sujal")
p.getDetails()
