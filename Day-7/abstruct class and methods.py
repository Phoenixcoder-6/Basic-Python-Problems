from abc import ABC, abstractmethod


class computer(ABC):
    @abstractmethod
    def process(self):     #abstruct method
        pass

class laptop(computer):
    def process(self):
        print("Its runningg")

#com= computer()
com1= laptop()
com1.process()
#com.process()