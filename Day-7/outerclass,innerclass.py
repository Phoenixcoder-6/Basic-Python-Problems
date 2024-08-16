class car():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.info= self.advanced_info()

    def showinfo(self):
        print(f"Name:{self.name},Price:{self.price}")
        self.info.showinfo()

    class advanced_info:
        def __init__(self):
            self.type="Electric"
            self.wheels= 4
            self.color= "Blue"

        def showinfo(self):
            print(f"Type:{self.type},Wheels={self.wheels}, Color:{self.color}")


s1= car("Audi",786907654)
s1.showinfo()

adv1= s1.info
print(id(adv1))


