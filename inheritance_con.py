class Animal:
    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def bark(self):
        return "Woof!"
    

class Cat(Animal):
    def meow(self):
        return "Meow"
    

dog = Dog()
cat = Cat()

print(dog.speak())
print(dog.bark())
print(cat.speak())
print(cat.meow())
print(cat.meow())
print(cat.meow())

class Car:
    def milage(self):
        return "car gives the good  milage"
  
class Ford(Car):
    def brand(self):
        return "Ford is good at built-quality"

class Mahendra(Car):
    def price(self):
        return "Mahendra is good at maketparice"
    def ower_ship(self):
        return "ower_ship is great"

class toyota(Mahendra):
    def build(self):
        return "Toyota is great at  the build-quality and features"
    def make(self):
        return __spec__,"is made in  the india."
    

ford = Ford()
Mahi = Mahendra()
toyo = toyota()



if __name__ == "__main__":
    print(ford.brand())
    print(Mahi.price())
    print(toyo.make())
        
