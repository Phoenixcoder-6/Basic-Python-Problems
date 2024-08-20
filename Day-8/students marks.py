class student:
    def __init__(self,name,roll,marks):
        self.name= name
        self.roll= roll
        self.marks= marks
    def getmarks(self):
        return self.marks        
    def getroll(self):
        return self.roll
    def __str__(self):
        return self.name + ':' + str(self.getroll())
    
def Marks(rec,name,roll,marks):
    rec.append(student(name,roll,marks))
    return rec

record=[]
x= 'y'
while x == 'y':
    name = input('Enter the name of the student: ')
    roll = input('Enter the roll number: ')
    marks = input('Marks: ')
    Record = Marks(record, name, roll, marks)
    x = input('another student? y/n: ')
    
# Printing the list of student
n = 1
for el in record:
    print(n,'. ', el)
    n = n + 1 