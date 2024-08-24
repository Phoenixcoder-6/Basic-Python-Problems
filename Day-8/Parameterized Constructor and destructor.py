class Person:
    def __init__(self):
        self.name=" "
        self.age=0
    def getInfo(self):
        self.name=input("Enter Name:")
        self.age= int(input("Enter age:"))
    def putInfo(self):
        print(f"{self.name} object created..")
        print(f"Name: {self.name}||Age:{self.age}")
    def __del__(self):
        print(f"{self.name} object deleted...")


p1=Person()
p1.getInfo()
p1.putInfo()

p2=Person()
p1.getInfo()
p2.putInfo()

del p1