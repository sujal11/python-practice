class Employee:
    salary=20000
    increment=2
    
    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,Sai):
      self.increment=Sai/self.salary 

a=Employee()
print(a.salaryAfterIncrement)
a.salaryAfterIncrement=3000
print(a.increment)
         