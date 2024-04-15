class Store:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):  # Corrected method name
        item = {'name': name, 'price': price}  # Corrected indentation
        self.items.append(item)  # Added item to the items list

    def stock_price(self):
        total = sum([item['price'] for item in self.items])  # Corrected list comprehension syntax
        return total
    
my_store = Store('my_store')

my_store.add_item('soap', 50)  # Corrected method name and added price
my_store.add_item('bag', 40)   # Corrected method name and added price

print("Total stock price:", my_store.stock_price())  # Added print statement to see the total stock price
