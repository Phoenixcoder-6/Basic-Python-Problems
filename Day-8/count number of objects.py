class student():
    counter=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.counter+=1
    def showstudent(self):
        print(f"{self.name} is {self.age} years old")

s1= student("Akai",21)
s2=student("Ajay",87)
print(student.counter)