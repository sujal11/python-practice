class Employee:     # --> Parents class
    company="Google"
    def __init__(self,name):
        self.name=name       
        
    #  Mulitilevel Inheritance --> when there is derived class is also a parents for another derived class      

class Programmer(Employee):   # --> Derived class of class Employee and parent class of class Student
    def getDetails(self):   
        print(f"The Employee Name Is {self.name} And His Company Is {self.company}")
        
class Student(Programmer):   # --> Derived class of class Programmer
    def getInfo(self):
        self.company="Youtube"
        print(f"The Student Name Is {self.name} And His Company Is {self.company}") 

  
p=Programmer("Sujal")
p.getDetails()
s=Student("SUJAL GARG")
s.getInfo()

