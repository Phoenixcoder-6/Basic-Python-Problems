class student:
    def __init__(self):
        self.name= " "
        self.roll=0
        self.marks= []
        self.total= 0
        self.per= 0
        self.grade= " "

    def setStudent(self):
        self.name= input("Enter the name of the student:")
        self.roll= int(input("Enter the roll:"))
        for i in range (5):
            mark = int(input(f"Enter marks for Subject {i+1}: "))
            self.marks.append(mark)
                                
    def total_marks(self):
        for x in self.marks:
            self.total=sum(self.marks)

    def calculatepercentage(self):
        if len(self.marks) == 5: 
            self.per=(self.total/500)*100

    def calculateGrade(self):
        if self.per>=85:
            self.grade="S"
        elif self.per>=75:
            self.grade="A"
        elif self.per>=65:
            self.grade="B"
        elif self.per>=55:
            self.grade="C"
        elif self.per>=50:
            self.grade="D"
        else:
            self.grade="F"

    def showstudent(self):
        self.total_marks()
        self.calculatepercentage()
        self.calculateGrade()
        print(f"name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Marks:{self.marks}")
        print(f"Total:{self.total}")
        print(f"Precentage:{self.per:.2f}%")
        print(f"Grade:{self.grade}")


def main():
    s=student()
    s.setStudent()
    s.showstudent()


if __name__=="__main__":
    main()



            
                                
        

    

