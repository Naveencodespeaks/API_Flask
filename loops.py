number = 7


while True:
    user_input = input("Would you like to play! (y/n)")
    if user_input == 'n':
        break

    user_number = int(input('Guess our number: '))
    if user_number == number:
        print("you guessed correctly! ")
    elif abs(number - user_number) == 1:
        print("you were off by one. ")
    else:
        print("sorry, it's wrong! ")
