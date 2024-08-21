class Person:
    def __init__(self,):
        self.name=" "
        self.age=0
    def getperson(self):
        self.name= input("Enter the name:")
        self.age= int(input("Enter age:"))
    def putperson(self):
        print(self.name,self.age)

    def gt(self,T):
        if self.age>T.age:
            return True
        else:
            return False
        
    def showresult(self,other):
        if self.gt(other):
            print(f"{self.name} is older than {other.name}.")
        elif other.gt(self):
            print(f"{self.name} is younger than {other.name}.")
        else:
            print(f"{self.name} and {other.name} both are equal.")
        
def main():
    p1=Person()
    p1.getperson()
    p2= Person()
    p2.getperson()

    p1.showresult(p2)

if __name__ == "__main__":
    main()

    