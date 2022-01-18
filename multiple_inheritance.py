class Employee:
    company="Google"
    def __init__(self,name):
        self.name=name
        

class Student:
    company="Youtube"        
        

class Programmer(Student,Employee):     # MULTIPLE INHERITANCE --> WHEN DERIVED CLASS HAVE MORE THAN ONE PARENT CLASS
    def getDetails(self):
        print(f"The employee name is {self.name} and his company is {self.company}")


p=Programmer("sujal")
p.getDetails()
