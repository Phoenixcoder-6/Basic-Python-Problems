class student:
    def getstudentinfo(self):
        self.rollno=input("Enter roll no:")
        self.name= input("Enter name:")
        self.phy= int(input("Enter Physics marks:"))
        self.chem= int(input("Enter Chemistry marks:"))
        self.math=int(input("Enter maths marks:"))

    def putstudent(self):
        print(f"Roll NO: {self.rollno}, Name : {self.name}")
        self.result()
    def result(self):
        total= self.phy + self.chem + self.math
        per = (int) (total/3)
        print("Percentage: ",per,end=",")
        if(per>=60):
            print("Result=Pass")
        else:
            print("Result= Fail")

studentlist = list()
while(True):
    s1=student()
    s1.getstudentinfo()
    studentlist.append(s1)
    n= input("Continue y/n?")
    if n=='n':
        break

for i in range(len(studentlist)):
    print("Student:",(i+1))
    studentlist[i].putstudent()

