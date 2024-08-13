from abc import ABC, abstractmethod
class veichle():
    def start(self,name=" "):
        print(name,"is started")
    @abstractmethod
    def acc(self,name=" "):
        pass
    @abstractmethod
    def park(self, name=" "):
        pass
    def stop(self,name=" "):
        print(name," stopped...")

class bike(veichle):
    def acc(self,name=" "):
        print(name,"is accelrating @90kmph")
    def park(self,name=" "):
        print(name,"is parked at 2 wheeler parking..")

def main():
    b=bike()
    b.start("bike")
    b.acc("bike") 
    b.park("bike")
    b.stop("bike") 


if __name__=="__main__":main()
