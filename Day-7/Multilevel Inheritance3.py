class Student:
    def __init__(self):
        self.__roll= 0
        self.__name=" "
    def getStudentInfo(self):
        self.__roll= int(input("Enter the roll number:"))
        self.__name= input("Enter the Name:")
    def printStudentInfo(self):
        print("Roll:",self.__roll)
        print("Name:",self.__name)

class Bsc(Student):
    def __init__(self):
        self.__pmarks=0
        self.__cmarks=0
        self.__mmarks=0
    def getBsc(self):
        self.getStudentInfo()
        self.__pmarks=int(input("Enter the Physics marks:"))
        self.__cmarks=int(input("Enter the Chemistry marks:"))
        self.__mmarks=int(input("Enter the Maths marks:"))
    def PutPerks(self):
        self.printStudentInfo()
        print("The Physics marks of the student:",self.__pmarks)
        print("The Chemistry  marks of the student:",self.__cmarks)
        print("The Mathematics marks of the student:",self.__mmarks)
    def calcTotalMarks(self):
        return (self.__pmarks+self.__cmarks+self.__mmarks)
    def average(self):
        return (self.__pmarks+self.__cmarks+self.__mmarks)/3
    

class Result(Bsc):
    def getResult(self):
        self.getBsc()
        self.__total=self.calcTotalMarks()
        self.__avg= self.average()

    def putResult(self):
        self.PutPerks()
        print("Total Marks out of 300 : ", self.__total)
        print(f"The average mark is: {self.__avg:.3f}")


student = Result()
student.getResult()
student.putResult()

