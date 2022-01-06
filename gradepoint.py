marks=int(input("Enter your marks to know the grade: "))
if(marks>=90):
    grade="O"
elif(marks>=80):
    grade="A"  
elif(marks>=70):
    grade="B"        
elif(marks>=60):
    grade="C"  
elif(marks>=50):
    grade="D"
else:
    grade="F"
print("your grade is "+grade)                  