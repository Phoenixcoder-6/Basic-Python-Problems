class vehicle:
    #constructor
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
class car(vehicle):
    def __init__(self,make,model,year,doors):
        super().__init__(make,model,year)
        self.doors=doors
        print(f"Car constructor: {self.year},{self.make},{self.model} with {self.doors} doors")

def main():
    print("Creating car object...")
    car1=car("Tyota","Corolla",2020,4)
    car1

if __name__=="__main__":
    main()