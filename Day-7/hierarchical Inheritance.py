class Employee:
    def __init__(self):
        self.__id=" "
        self.__name= " "
        self.__gender= " "
    def getEmployee(self):
        self.__id= input("Enter the ID:")
        self.__name= input("Enter the name:")
        self.__gender=input("Enter the gender:")
    def showEmployee(self):
        print("ID:", self.__id)
        print("Name:",self.__name)
        print("Gender:",self.__gender)

class Doctor(Employee):
    def __init__(self):
        super().__init__()
        self.__dept= " "
        self.__comp= " "
    def getDoctor(self):
        self.getEmployee()
        self.__dept= input("Enter the Department:")
        self.__comp= input("Enter the company name:")
    def showDoctor(self):
        self.showEmployee()
        print("Department:",self.__dept)
        print("Company:",self.__comp)
class Engineer(Employee):
    def __init__(self):
        super().__init__()
        self.__dept= " "
        self.__comp= " "
    def getEngineer(self):
        self.getEmployee()
        self.__dept= input("Enter the Department:")
        self.__comp= input("Enter the company name:")
    def showEngineer(self):
        self.showEmployee()
        print("Department:",self.__dept)
        print("Company:",self.__comp)

def main():
    print("\nDoctor Object..")
    d= Doctor()
    d.getDoctor()
    d.showDoctor()
    print("\n Engineer Object..")
    e= Engineer()
    e.getEngineer()
    e.showEngineer()

if __name__=="__main__":
    main()




