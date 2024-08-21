class Distance:
    def __init__(self, Km,M,Cm):
        self.km=Km
        self.m=M
        self.cm=Cm
    def getKm(self):
        return self.km
    def getM(self):
        return self.m
    def getCm(self):
        return self.cm
    
    def __add__(self,other):
        km=self.km+ other.km
        m=self.m + other.m
        cm= self.cm + other.cm
        s3= Distance(km,m,cm)
        return s3

d1=Distance(45,43,21)
d2=Distance(34,21,54)

d3= d1+d2

print("The new distance:\n")
print("Km:", d3.km)
print("M:", d3.m)
print("Cm:", d3.cm)

