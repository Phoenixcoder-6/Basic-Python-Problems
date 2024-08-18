class Details1:
    def __init__(self):
        self.__id= " "
    def setDetails1(self):
        self.__id= input("Enter the id:")
    def showDetails1(self):
        print("The Student details are:")
        print("ID:",self.__id)
class Details2(Details1):
    def __init__(self):
        self.__name= ""
    def setDetails2(self):
        self.setDetails1()
        self.__name= input("Enter the name:")
    def showDetails2(self):
        self.showDetails1()
        print("Name:",self.__name)

class Details3(Details2):
    def __init__(self):
        self.__gender=""
    def setDetails3(self):
        self.setDetails2()
        self.__gender= input("Enter the gender:")
    def showDetails3(self):
        self.showDetails2()
        print("Gender:",self.__gender)

class Student(Details3):
    def __init__(self):
        self.__designation=" "
        self.__dept=" "
    def setStudent(self):
        self.setDetails3()
        self.__designation= input("Enter the designation:")
        self.__dept=input("Enter the department:")
    def showStudent(self):
        self.showDetails3()
        print("Department:",self.__dept)
        print("Designation:", self.__designation)

def main():
    s=Student()
    s.setStudent()
    s.showStudent()

if __name__=="__main__":
    main()


    


