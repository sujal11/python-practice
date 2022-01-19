from ast import Pass


class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost, premium_amount):
        
        self.vehicle_id=vehicle_id
        self.vehicle_type=vehicle_type
        self.vehicle_cost=vehicle_cost
        self.premium_amount=premium_amount
        
    def display_vehicle_cost(self):
        if(self.vehicle_type=="Two wheeler"):
            self.premium_amount=self.vehicle_cost*2/100
        elif(self.vehicle_type=="Four wheeler"):
            self.premium_amount=self.vehicle_cost*6/100
        else:
            print("Invalid vehicle type")    
    def display_vehicle_details(self):
        return self.premium_amount
        
V=Vehicle(23,"Two wheeler",50000,None)
V.display_vehicle_cost()
print(V.display_vehicle_details())