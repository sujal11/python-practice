sub1=int(input("Enter your sub1 marks in %: "))
sub2=int(input("Enter your sub2 marks in %: "))
sub3=int(input("Enter your sub3 marks in %: "))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are failed because your marks is less than 33")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are failed because your total percentage is less than 40")    
else:
    print("you are passed")    