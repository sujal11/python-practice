class Employee:
    company="Google"
    def __init__(self,name):
        self.name=name       
        
#  Mulitilevel Inheritance --> when there is more than one derived class of single base class       

class Programmer(Employee):     
        print(f"The Employee Name Is {self.name} And His Company Is {self.company}")
        
class Student(Employee):  
    def getInfo(self):
        self.company="Youtube"
        print(f"The Student Name Is {self.name} And His Company Is {self.company}") 


p=Programmer("Sujal")
p.getDetails()
s=Student("SUJAL GARG")
s.getInfo()

