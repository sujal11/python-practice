class Programmer:
    company="Microsoft"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(f"the name of programmer is {self.name} and age is {self.age}")

Programmer1 = Programmer("Sujal",20)
Programmer2 = Programmer("Sonakshi",19)
Programmer3 = Programmer("Sujal2",20)
Programmer1.display()    
Programmer2.display()    
Programmer3.display()    

        
        

        

