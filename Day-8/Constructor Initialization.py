class Person:
    def __init__(self):
        self.name=" "
        self.age=0
    def getInput(self):
        self.name= input("Enter Name")
        self.age=int(input("Enter age:"))
    def putInfo(self):
        print(f"Name: {self.name} Age: {self.age}")


p1=Person()
p1.getInput()
p1.putInfo()