class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books."
    
shelf = Bookshelf(300)
print(shelf)


class Car:
    def __init__(self,name, make, year):
        self.name = name
        self.make = make
        self.year = year
    def __str__(self):
        return f"what is the name of the car? {self.name} and make of the car is {self.make}, and in which year car is manufactured {self.year}"
    

car_details = Car("ford","Endeavour", 2024)

print(car_details)


