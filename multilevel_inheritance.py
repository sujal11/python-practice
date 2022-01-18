class Employee:
    company="Google"
    def __init__(self,name):
        self.name=name       
        

class Programmer(Employee):     # MULTIPLE INHERITANCE --> WHEN DERIVED CLASS HAVE MORE THAN ONE PARENT CLASS
    def getDetails(self):
        print(f"The Employee Name Is {self.name} And His Company Is {self.company}")
        
class Student(Employee):
    def getInfo(self):
        self.company="Youtube"
        print(f"The Student Name Is {self.name} And His Company Is {self.company}")


p=Programmer("Sujal")
p.getDetails()
s=Student("SUJAL GARG")
s.getInfo()

