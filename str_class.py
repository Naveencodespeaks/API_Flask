class Student:
    def __init__(self,name,session,rollno,class_room):
        self.name = name
        self.session = session
        self.rollno = rollno
        self.class_room = class_room

    def __str__(self):
        return f"{self.name} class room no: {self.class_room} and his rollno is {self.rollno} and his {self.session}"
    

student_detials = Student('Naveen','10th-A', 123456, 2)
print(student_detials)