class vehicle:
    def __init__(self,brand,type):
        self.brand=brand
        self.type=type

class car(vehicle):
    def __init__(self,brand,type,wheels,price):
        super().__init__(brand,type)
        self.wheels=wheels
        self.price=price
class bike(vehicle):
    def __init__(self,brand,type,wheels,price):
        super().__init__(brand,type)
        self.wheels=wheels
        self.price=price


c1=bike("Audi","Petrol",2,"90k")
c2= car("Nexa","Electric",4,"108k")

print(c1.type)


    
    