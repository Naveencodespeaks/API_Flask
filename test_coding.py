class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, name, price):  # Changed method name to add_items
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        total_price = sum(item['price'] for item in self.items)  # Fixed variable name in list comprehension
        return total_price

# Create an instance of the Store class
mystore = Store("my_store")

# Add items to the store
mystore.add_items("soap", 20)
mystore.add_items("bag", 100)  # Fixed syntax
mystore.add_items("bottel", 40)  # Fixed syntax

# Print the total stock price
print("Total stock price:", mystore.stock_price())  # Fixed print statement
