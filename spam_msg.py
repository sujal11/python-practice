text=input("Enter your text: ")
spam = False
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("Subscribe this" in text):
    spam=True 
else:
    spam=False       
print("This spam comment is: ",spam)        