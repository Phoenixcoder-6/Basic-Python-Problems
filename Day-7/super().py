class car():
    def __init__(self,type):
        self.type= type

    @staticmethod
    def start():
        print("car started..")

    def stop(self):
        print(f"{self.stop} car stopped")

class Audi(car):
    def __init__(self,name,type):
        self.name= name
        super().__init__(type)

    def showresults(self):
        print(f"{self.name} car started...")

car1= Audi("nexa","petrol")
print(car1.showresults())