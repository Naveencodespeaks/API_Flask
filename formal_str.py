class Car:
    def __init__(self,name, brand,model,engin, seats):
        self.name = name 
        self.brand = brand
        self.model = model
        self.engin =  engin
        self.seats = seats
    def __str__(self):
        return (f"Name of the car is {self.name}, and this car belongs to the {self.brand} and it is {self.seats} car and has a {self.engin} engin.")
    
car_details = Car("Endeavour","Ford", "Top-End", "v8", 7)

print(car_details)
