users = [

    (0,"Kesava","password"),
    (1,"krishna","mail_id"),
    (2, "Rama", "password"),
    (3, "govinda", "madhusudhana"),
    (4, "Raghurama", "123"),
]

user_mapping  = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_,username, password = user_mapping[username_input]

if password_input == password:
    print("Your details are correct! ")
else:
    print("your details are incorrect! ")