class car():
    def __init__(self,info):
        self.info=info
    def execute(self):
        print(f"{self.info} Car started..")
        print("Car stopped..")


class engine():
    def specifications(self,type):
        type.execute()


car1=car("Electric")
ca= engine()

ca.specifications(car1)