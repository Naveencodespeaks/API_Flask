from typing import List, Optional

class Student:
    def __init__(self,name:str, grades:Optional[list[int]]= None):
        self.name = name
        self.grades = grades or []

    def take_exam(self,result:int):
        self.grades.append(result)
bob = Student("Bob",[13,45])
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)