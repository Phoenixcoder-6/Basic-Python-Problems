# Base class 1
class Engine:
    def type(self, engine_type):
        self.engine_type = engine_type
    
    def start_engine(self):
        print(f"The {self.engine_type} engine has started.")

# Base class 2
class Transmission:
    def engine(self, name):
        self.name = name
    
    def engage_transmission(self):
        print(f"The {self.name} transmission is engaged.")

# Derived class
class Car(Engine, Transmission):
    def __init__(self, engine_type, name, model):
        self.type(engine_type)  # Calls the type method from Engine class
        self.engine(name)  # Calls the engine method from Transmission class
        self.model = model

    def display_details(self):
        print(f"Car Model: {self.model}")
        print(f"Engine Type: {self.engine_type}")
        print(f"Transmission Name: {self.name}")

# Creating an instance of Car
my_car = Car("V8", "Automatic", "Mustang")
my_car.display_details()
my_car.start_engine()
my_car.engage_transmission()
