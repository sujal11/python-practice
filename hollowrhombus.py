n=int(input("Enter the number "))
m=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,m+1):
        if(i==n or j==m or j==1 or i==1):
            print("*",end="")
        else:
            print(" ",end="") 
    print()

    

