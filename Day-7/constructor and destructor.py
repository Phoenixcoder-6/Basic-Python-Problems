class car():
    #constructor
    def __init__(self,model,type):
        self.model= model
        self.type= type
        print(f"A new car has been created: {self.model} {self.type}")
    #desturctor
    def __del__(self):
        print(f"{self.model} and {self.type} has deleted..")

    #method to display class details
    def displaydetails(self):
        print(f"Car Details: Model = {self.model}, Type = {self.type}")

# Creating an instance of Car
my_car = car("Toyota", "Electric")
my_car.displaydetails()

del(my_car)