from binascii import b2a_hex


def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
x=int(input("Enter the number "))
y=int(input("Enter the number "))
z=int(input("Enter the number "))
max=greatest(x,y,z)        
print(max,"is the greatest")


