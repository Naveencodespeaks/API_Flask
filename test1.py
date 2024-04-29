class Car:
    def __init__(self,name, brand, seater, model, price):
        self.name = name
        self.brand = brand
        self.seater = seater
        self.model = model
        self.price = price

car_details = Car("Endeavour","Ford", 5, "SUV", '25,000,00 lakhs')


if __name__ == "__main__":
    print(f"'{car_details.brand}' is the Brand of the car.")
    print(f"{car_details.name} is the Name of the car.")
    print(f"{car_details.seater} is the no of seats in the car.")
    print(f"{car_details.model} is the model of the car.")
    print(f"{car_details.price} is the on-road price of the car.")