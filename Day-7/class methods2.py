class Student():
    school="ABC"

    def __init__(self,m1,m2,m3):
        self.m1=m1                     #instance method
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1 + self.m2+self.m3)/3
    
    @classmethod                       #classmethod
    def showinfo(cls):
        return cls.school
    
    @staticmethod
    def type():
        print("This is a registered student")

    
s1=Student(32,34,54)
print(s1.avg())
print(Student.showinfo())
print(s1.type())