class Student:
    def getStudentDetails(self):
        self.rollno=input("Enter Roll Number : ")
        self.name = input("Enter Name : ")
        self.physics =int(input("Enter Physics Marks : "))
        self.chemistry = int(input("Enter Chemistry Marks : "))
        self.maths = int(input("Enter Math Marks : "))
    def calculatepercentage(self):
        self.percentage= (int) (self.physics+ self.chemistry + self.maths)/300 * 100
        return self.percentage
    def grace(self):
        if self.physics <= self.chemistry and self.physics <= self.maths:
            self.physics += 9
        elif self.chemistry <= self.physics and self.chemistry <= self.maths:
            self.chemistry += 9
        else:
            self.maths += 9
    
    def showdetails(self):
        original_percentage = self.calculatepercentage()
        print(f"Name:{self.name} |Roll :{self.rollno} | Percentage: {original_percentage:.2f}%")
        self.grace()
        print(f"Marks after grace: Physics: {self.physics}, Chemistry: {self.chemistry}, Maths: {self.maths}")


def main():
    s1=Student()
    s1.getStudentDetails()
    #s1.calculatepercentage()
    s1.showdetails()

if __name__ == "__main__":
    main()
