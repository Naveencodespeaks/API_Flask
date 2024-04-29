class Book:
    TYPES = ("hardcover","Paperback")


    def __init__(self, name,book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    def __rep__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

book = Book("Harry Potter", "Paperback", 1500)
print(book.name)
print(book.book_type)
print(book)
print(book.weight)