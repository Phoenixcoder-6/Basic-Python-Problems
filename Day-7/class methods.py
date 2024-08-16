class car():
    name="Audi"

    def changename(self,name):
        self.name=name
        car.name=name

p1=car()
p1.changename("nexa")
print(p1.name)
print(car.name)
