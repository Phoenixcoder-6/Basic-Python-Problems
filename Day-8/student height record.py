class student:
    def __init__(self,name,height):
        self.name=name
        self.height= height
    def showstudent(self):
        print(f"Name:{self.name}, Height:{self.height}\n")

def main():
    s1=student("Anisha Samanta", " 5'2''" )
    s1.showstudent()
    s2=student("Deba Roy", " 5'6'' ")
    s2.showstudent()

if __name__ == "__main__":
    main()
