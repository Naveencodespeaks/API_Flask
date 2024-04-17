from libs import operator


print("mylib.py:", __name__)

class Car:
    def __init__(self, name, make,place):
        self.name = name
        self.make  = make
        self.place = place
    