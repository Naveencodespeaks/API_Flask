class Car:
    def __init__(self, brand, name_of_car, price, engin, tyre):
        self.brand = brand
        self.name_of_car = name_of_car
        self.price = price
        self.enign = engin
        self.seat = tyre
    def __str__(self):
        return f"Name of the car is {self.name_of_car} it belongs to the {self.brand!r}: brand, the cost of the car is {self.price} The no of tyres are {self.seat}"
    

car_details = Car('Ford','Endeavour', '30,Lakhs','v8', 4)
print(car_details)