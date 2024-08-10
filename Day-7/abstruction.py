class Car():
    def __init__(self):
        self.brk=True
        self.clutch=False
        self.acc= False

    def start(self):
        self.brk=False
        self.acc= True
        print("Car Started...")

c1= Car()
c1.start()