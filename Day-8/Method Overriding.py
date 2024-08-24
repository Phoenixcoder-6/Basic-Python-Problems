class Father:
    def showPhone(self):
        print("I have Nokia Phone..")
class Son1(Father):
    pass
class Son2(Father):
    def showPhone(self):
        print("I have apple phone")

print("Father object created..")
p1=Father()
p1.showPhone()
print("Son1 object created..")
p2=Son1()
print(p2.showPhone())
print("Son2 object created..")
p3=Son2()
print(p3.showPhone())
    