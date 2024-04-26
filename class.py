class Car:
    def __init__(self,name, make, model,  milage, price):
        self.name = name 
        self.make = make
        self.model = model
        self.milage = milage
        self.price = price


car_details = Car('ford',2024,'Endeavour','25kml','30lakhs' )


if __name__ == "__main__":
    print(car_details.name)
    print(car_details.make)
    print(car_details.model)
    print(car_details.milage)
    print(car_details.price)

