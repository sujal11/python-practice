class Complex_num:
    def __init__(self,r,i):
        self.real=r
        self.imag=i

    def __add__(self,c):
        return Complex_num(self.real+c.real,self.imag+c.imag)  

    def __mul__(self,c):      
        # **** FORMULAE  FOR MULTIPLICATION OF 2 COMPLEX NUMBERS  ****
        # (a+bi) (c+di) = (ac-bd) + (ad+bc)i
        mulReal = (self.real*c.real)-(self.imag*c.imag)
        mulImaginary = (self.real*c.imag)+(self.imag*c.real)  

        return Complex_num(mulReal,mulImaginary)      

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1=Complex_num(3,4)
c2=Complex_num(4,5)
print(c1+c2)
print(c1*c2)    