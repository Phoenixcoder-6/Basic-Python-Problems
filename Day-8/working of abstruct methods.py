from abc import ABC,abstractmethod

class student:
    @abstractmethod
    def getinfo(self):
        pass
    @abstractmethod
    def putinfo(self):
        pass

class bsc(student):
    def getinfo(self):
        self.__roll = input("Enter Roll : ")
        self.__name = input("Enter Name : ")

        self.__p = int(input("Enter Physics : "))
        self.__c = int(input("Enter Chemistry : "))
        self.__m = int(input("Enter Maths : "))
    def putinfo(self):
        print(self.__roll, self.__name)
        print("Percentage : ", ((self.__p + self.__c + self.__m)/3))



s1=bsc()
s1.getinfo()
s1.putinfo()