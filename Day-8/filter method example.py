class Student:
    def getStudentInfo(self):
        self.rollno = input("Enter roll no: ")
        self.name = input("Enter Name: ")
        self.percentage = int(input("Enter percentage: "))

    def printStudentInfo(self):
        print("Roll No: ", self.rollno)
        print("Name: ", self.name)
        print("Percentage: ", self.percentage)

    def search(self, minMarks):
        if self.percentage >= minMarks:
            return True
        else:
            return False
        
s1 = []
while True:
    student = Student()
    student.getStudentInfo()
    s1.append(student)
    
    ch = input("Continue y/n? ")
    if ch.lower() == 'n':
        break

minPercent = int(input("Enter Qualifying Percentage: "))

# Corrected the method name from `Search` to `search`
FL = list(filter(lambda s: s.search(minPercent), s1))
if len(FL) == 0:
    print('No Record Exist')
else:
    print("Students qualified are:")
for s in FL:
    s.printStudentInfo()