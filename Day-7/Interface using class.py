from abc import ABC, abstractmethod

# Define the abstract base class (interface)
class animal():
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sound(self):
        pass

class Tiger(animal):
    def eat(self,food=" "):
        self.food= food
        print(f"Tiger eats:{self.food}")
    def sound(self,snd= " "):
        self.snd=snd
        print(f"Tiger sounds: {self.snd}")

c1= Tiger()
c1.eat("Chicken")
c1.sound("meaw")
