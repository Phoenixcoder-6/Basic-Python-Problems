class Student:
    def getStudent(self):
        self.__rollno = input("Enter Roll No: ")
        self.__name = input("Enter Name: ")
        self.__phy = int(input("Enter Physics Marks: "))
        self.__chem = int(input("Enter Chemistry Marks: "))
        self.__math = int(input("Enter Maths Marks: "))
        self.result()

    def putStudent(self):
        print("Roll Number: ", self.__rollno, end = " ")
        print("Name: ", self.__name, end = " ")
        print("Percentage: ", self.__percentage, end = " ")
        if (self.__percentage >= 60):
            print("Pass")
        else:
            print("Fail")

    def result(self):
        total = self.__phy + self.__chem + self.__math
        self.__percentage = (int)(total / 3)
            
    def search(self,min,max):
         if(self.__percentage>=min and self.__percentage<=max):
             return True
         else:
             return False

studentList = list()

while(True):
    studentObject=Student()
    studentObject.getStudent()
    studentList.append(studentObject)
    ch=input("Continue y/n? ")
    if ch == 'n':
        break
    
min=int(input("Enter Min Percentage: "))
max=int(input("Enter Max Percentage: "))

searchList = list()
for studentObject in studentList:
    found=studentObject.search(min,max)
    if(found):
        searchList.append(studentObject)
if(len(searchList)==0):
    print('No Record Exist')
else:
 for studentObject in searchList:
    studentObject.putStudent()
