class Student:
    def __init__(self,name,id,email,phone):
        self.name = name
        self.id = id
        self.email = email
        self.phone = phone


stuend_details = Student("Naveen", 502, "sainaveen@gmail.com", 1234567)

stuend_details.name
print(stuend_details.id)
print(stuend_details)

if __name__ == "__main__":
    #stuend_details
    stuend_details