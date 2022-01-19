# Q1: For a given list of numbers, find its factors and add the factors. Then if the sum of factors is present in the original list, sort it and print it else print -1.
#if x is perfectly divisible by i, then i is a factor of x.
def findFactSum(n):
    s=1
    for j in range(2,n+1):
        if(n%j==0):
            s+=j
    return s
result=[]
L=list(map(int,input()))    
for i in L:
    val=findFactSum(i)
    if val in L:
        result.append(i)
if(len(result)==0):
    Print("-1")
else:
    print(sorted(result))    

