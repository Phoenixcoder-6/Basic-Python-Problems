class car():
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car Stopped...")

class Tyotacar(car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Tyotacar):
    def __init__(self,type):
        self.type=type

car1= Fortuner("Electric")
car1.start()