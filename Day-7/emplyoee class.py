class emplyoee():
    def __init__(self,id,name,age,post):
        self.id= id
        self.name=name
        self.age=age
        self.post= post

    def showinfo(self):
        print(f"name:{self.name},Emplyoee id={self.id}, age={self.age}, Post={self.post}")

e1= emplyoee("E001","Ajay Kumar", 34, "Analyst")
print(e1.showinfo())