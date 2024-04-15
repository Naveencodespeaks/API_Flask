class ClassTest:
    def instance_method(self):
        return f"Called instance_method of {self}"
    
    

test = ClassTest()
test.instance_method()  # Calling instance method using instance
ClassTest.instance_method(test)  # Also calling instance method using instance

print(test)  # Printing the string representation of the object
