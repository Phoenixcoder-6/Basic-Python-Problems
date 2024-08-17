class car():
    def __init__(self,color,brand):
        self.color= color
        self.brand=brand


class tyotacar(car):
    def __init__(self,color,brand,type):
        super().__init__(color,brand)
        self.type=type

car1=tyotacar("Blue","Audi","Electric")
print(car1.color)
print(car1.brand)
print(car1.type)
