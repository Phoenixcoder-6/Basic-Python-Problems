class menuitem:
    def __init__(self,name,price):
        self.name=name
        self.price= price
    def getprice(self):
        return self.price
    def __str__(self):
        return self.name + ': ' + str(self.getprice())
    
def chart(ref,name,price):
    ref.append(menuitem(name,price))
    return ref

ref = []
x = 'y'
while x=='y':
    name= input("Enter item name: ")
    price=int(input("Enter price:"))
    ref = chart(ref,name,price)
    x= input('Another item? y/n ')

n=1
for el in ref:
    print(f"{n}.{el}")
    n=n+1
