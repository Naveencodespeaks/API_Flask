def hello(): # callable  variable
    print('Hello')



hello()

def user_age_in_seconds():
    user_age = int(input('Enter your age:'))
    age_secondss = user_age *365 *24 * 60 * 6

    print(f"you age in seconds is {age_secondss}")

    user_age_in_seconds()
    print('Goodbye!')

