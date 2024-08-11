class student():
    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno


s1= student("Ankita",10911223001)
print(s1.name,s1.rollno)

del(s1.name)
#print(s1.name)
print(s1.rollno)