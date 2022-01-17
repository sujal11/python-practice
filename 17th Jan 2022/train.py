from traceback import print_exception


class Train:
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare 

    def getInfo(self):
        print(f"The train name is {self.name}")
        print(f"Seat available in train are {self.seats}")
        print(f"The fare of your ticket is Rs {self.fare}")
    
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked and your seat no. is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry the train is full!")    
    


a=Train("RAJDHANI EXPRESS",50,250)
a.getInfo()
a.bookTicket()
a.getInfo()

