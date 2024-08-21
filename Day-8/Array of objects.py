class Student:
    def getStudentinfo(self):
        self.rollno= input("Enter roll number:")
        self.name=input("Enter Name:")
        self.Geo= int(input("Enter Geography marks:"))
        self.Hist= int(input("Enter History marks:"))
        self.Beng= int(input("Enter Bengali marks:"))
    def printResult(self):
        print(self.rollno,self.name,((int)( (self.Geo+self.Hist+self.Beng)/300*100 )))

Studentarray=[]
while(True):
    s1=Student()
    s1.getStudentinfo()
    Studentarray.append(s1)
    ch = input("Add More y/n?")
    if(ch=='n'):break

print("Results : ")

for student in Studentarray:
    student.printResult()
