class twosum:
    def getnum(self):
        self.x=int(input("Enter value of x:"))
        self.y=int(input("Enter value of y:"))

    def putnum(self):
        print("value of x = ", self.x,"value of y = ", self.y )

    def Add(self,T):
        R=twosum()
        R.x=self.x+T.x
        R.y=self.y+T.y
        return R

obj1 = twosum()
obj2 = twosum()
print("Enter values of object 1 ")
obj1.getnum()
print("Enter values of object 2 ")
obj2.getnum()
obj3 = obj1.Add(obj2)
print("Values of object 1 ")
obj1.putnum()
print("Values of object 2 ")
obj2.putnum()
print("Values of object 3 (sum object) ")
obj3.putnum()