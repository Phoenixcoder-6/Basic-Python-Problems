class Media:
    def __init__(self):
        self.title= " "
        self.price= 0
    def getMediaInfo(self):
        self.title= input("Enter Title:")
        self.price= int(input("Enter price:"))
    def putMediaInfo(self):
        print(self.title,self.price)
class Magazine(Media):
    def getMagazineInfo(self):
        self.getMediaInfo()
        self.pages=int(input("Enter pages:"))
    def putMagazineInfo(self):
        self.putMediaInfo()
        print("Pages:",self.pages)
class Channel(Media):
    def getChannelInfo(self):
        self.getMediaInfo()
        self.freq= input("Enter frequency:")
    def putChannelInfo(self):
        print("---Channel Info---")
        self.getMediaInfo()
        print("Frequency:",self.freq)

print("Enter Magazine Information:")
m1= Magazine()
m1.getMagazineInfo()
m1.putMagazineInfo()

print("Enter Channel Information:")
m2= Channel()
m2.getChannelInfo()
m2.putChannelInfo()



