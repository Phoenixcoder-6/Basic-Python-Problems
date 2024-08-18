class personel:
    def __init__(self):
        self.__id=0
        self.__name=""
        self.__gender= ""

    def setpersonel(self):
        self.__id= int(input("Enter the ID:"))
        self.__name= input("Enter Name:")
        self.__gender= input("Enter Gender:")
    
    def showpersonel(self):
        print("Id: ",self.__id)
        print("Name:",self.__name)
        print("Gender: ",self.__gender)

class Educational:
    def __init__(self):
        self.__stream=""
        self.__year=""
    def setEducational(self):
        self.__stream= input("Enter the stream:")
        self.__year= input("Enter year:")
    def showEducational(self):
        print("Stream: ", self.__stream)
        print("Year: ", self.__year)

class Student(personel,Educational):
    def __init__(self):
        self.__address= " "
        self.__contact= " "
    def setStudent(self):
        self.setpersonel()
        self.setEducational()
        self.__address= input("Enter Address:")
        self.__contact= input("Enter the contact:")
    def showStudent(self):
        self.showpersonel()
        self.showEducational()
        print("Address:",self.__address)
        print("Contact:",self.__contact)

def main():
    s=Student()
    s.setStudent()
    s.showStudent()

if __name__=="__main__":
    main()

