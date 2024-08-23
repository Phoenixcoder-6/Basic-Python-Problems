class car:
    def __init__(self,model,wheels,price):
        self.model= model
        self.wheels=wheels
        self.price= price
    def __str__(self):
        return f"Model:{self.model} | Wheels:{self.wheels} | Price:{self.price}"

def details(rec,model,wheels,price):
    rec.append(car(model,wheels,price))
    return rec

record=[]
x= 'y'
while x == 'y':
    model = input('Enter the model of the car: ')
    wheels = input('Enter the no of wheels: ')
    price = input('price ')
    Record = details(record, model, wheels, price)
    x = input('another car? y/n: ')
    
# Printing the list of student
n = 1
for el in record:
    print(n,'. ', el)
    n = n + 1 


r= input("enter the model:")
for c in record:
    if c.model==r:
        print(c)
    else:
        print("Car not found")