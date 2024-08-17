class employee:
    def __init__(self):   #constructor
        self.__id=0
        self.__name= ""
        self.__sex=""
        self.__city=""
        self.__salary=""
        print("Object Initialized...")

    def __del__(self):
        print("Object destroyed..")

    def setData(self):
        self.__id=int(input("Enter ID\t:"))
        self.__name= input("Enter Name\t:")
        self.__sex=input("Enter sex\t:")
        self.__city=input("Enter City\t:")
        self.__salary=int(input("Enter salary\t:"))

    def showData(self):
        print("Id\t\t:",self.__id)
        print("Name\t:", self.__name)
        print("SEX\t:",self.__sex)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)

    def __str__(self):
        return f"employee[ID={self.__id}, Name={self.__name}, Sex={self.__sex}, City={self.__city}, Salary={self.__salary}]"


def main():
    #Employee Object
    emp=employee()
    emp.setData()
    emp.showData()
    print(emp)

if __name__=="__main__":
    main()
