def factorial(n):
   if(n==0 or n==1):
       return 1
   else:
       return n*factorial(n-1)    
n=int(input("Enter the number: "))
print(factorial(n))      