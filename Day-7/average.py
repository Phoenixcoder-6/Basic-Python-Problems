class Student():
    def __init__(self):
        self.name=""
        self.roll=0
        self.marks=[]
        self.total=0
        self.result=0

    def setstudent(self):
        self.name=input("Enter the name of the student:")
        self.roll=int(input("Enter the roll of the student:"))
        for i in range(3):
            mark= int(input(f"Enter the marks for subject {i+1}:"))
            self.marks.append(mark)
    def average(self):
        self.total= sum(self.marks)
        self.result= self.total/3
    
    def showstudent(self):
        self.average()
        print(f"name:{self.name}")
        print(f"Roll:{self.roll}")
        print(f"marks:{self.marks}")
        print(f"Total number: {self.total}")
        print(f"Average is: {self.result:0.2f}")

def main():
    s= Student()
    s.setstudent()
    s.showstudent()
if __name__=="__main__":
    main()

