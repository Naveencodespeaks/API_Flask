class Person:
    def __init__(self,name, age): # name, age are know as parameters
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age}, years old"
    
    def __repr__(self):
        return f"<person({self.name},{self.age})> "

#bob_name is know as the objects
bob_name  = Person("bob", 35) 
print(bob_name)

