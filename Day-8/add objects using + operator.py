class TwoNum:
    def getValue(self):
        self.x= int(input("Enter X:"))
        self.y= int(input("Enter Y:"))
    def putValue(self):
        print(self.x,self.y,"sum:",(self.x+self.y))

    def __add__(self,other):
        R=TwoNum()
        R.x= self.x + other.x
        R.y=self.y + other.y
        return R
    

obj1= TwoNum()
print("Object 1:")
obj1.getValue()
obj1.putValue()


obj2= TwoNum()
print("Object 2:")
obj2.getValue()
obj2.putValue()

sumObj= obj1 +obj2
sumObj.putValue()



