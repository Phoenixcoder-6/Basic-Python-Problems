class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} can make a sound."
class Mammal(Animal):
    def __init__(self,name,fur_color):
        super().__init__(name)
        self.fur_color= fur_color
    def describe(self):
        return f" {self.name} is a mammal with {self.fur_color} fur."
    
class Dog(Mammal):
    def __init__(self,name,fur_color,breed):
        super().__init__(name,fur_color)
        self.breed=breed
    def bark(self):
        return f"{self.name} the {self.breed} barks loudly!"
    

d1= Dog("Rahul","White","Weimaraner")
print(d1.speak())
print(d1.describe())
print(d1.bark())