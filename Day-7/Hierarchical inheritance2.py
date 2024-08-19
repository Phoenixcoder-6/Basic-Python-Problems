class student:
    def __init__(self):
        self.__rollNo=0
        self.__name=" "
    def getStudentInfo(self):
        self.__rollNo= int(input("Enter the roll number:"))
        self.__name= input("Enter the name:")
    def showStudent(self):
        print(f"Printing details of {self.__name}.")
        print("Roll number :",self.__rollNo)
        print("Name:",self.__name)

class Bsc(student):
    def __init__(self):
        super().__init__()
    def getBsc(self):
        self.getStudentInfo()
        self.__p=int(input("Enter Physics marks:"))
        self.__c=int(input("Enter Chemistry marks:"))
        self.__m=int(input("Enter Maths marks:"))

    def showBsc(self):
        self.showStudent()
        print("Physics:",self.__p)
        print("Chemistry:",self.__c)
        print("Mathematics:",self.__m)

class Ba(student):
    def __init__(self):
        super().__init__()
    def getBa(self):
        self.getStudentInfo()
        self.__h=int(input("Enter History marks:"))
        self.__g=int(input("Enter Geography  marks:"))
        self.__e=int(input("Enter Economics marks:"))

    def showBa(self):
        self.showStudent()
        print("History:",self.__h, "Geography:",self.__g,"Economics:",self.__e)
def main():
    print("\nBSC object created...")
    b=Bsc()
    b.getBsc()
    b.showBsc()
    print("\nBA object created...")
    ba=Ba()
    ba.getBa()
    ba.showBa()


if __name__ =="__main__":
    main()



        