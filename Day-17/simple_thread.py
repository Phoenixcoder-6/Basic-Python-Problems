from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello!!")

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi!!!")


t1= hello()
t2= hi()

t1.start()
t2.start()