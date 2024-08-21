class Phone:
    def __init__(self,Phonename,model,price):
        self.Phonename=Phonename
        self.model=model
        self.price=price
    def getmodel(self):
        return self.model
    def getprice(self):
        return self.price
    def __str__(self):
        return self.Phonename + ':' + str(self.getmodel()) + ' :: '+ str(self.getprice())
    
def prices(rec, Phonename,model,price):
    rec.append(Phone(Phonename,model,price))
    return rec

record=[]
x= 'y'
while x=='y':
    Phonename= input("Enter the phone name:")
    model=input("Enter the model name: ")
    price= input("Enter the price of that phone:")
    record= prices(record,Phonename,model,price)
    x= input("Another item?? y/n")
n=1
print("----The list----")
for ele in record:
    print(n,'.',ele)
    n+=1