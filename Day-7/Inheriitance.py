class car():
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car stopped..")

class Tyotacar(car):
    def __init__(self,name):
        self.name= name


car1= Tyotacar("Fortuner")
car2=Tyotacar("Maruti")

car1.start()
car2.stop()