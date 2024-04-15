friends = ["Hare", "Krishna", "Madava"]

print('Krishna' in friends)

movies_watched = {"The Matrix", "Green book", "Her"}

user_movies = input("Enter something you've watched recently! ")

print(user_movies in movies_watched)


if user_movies in movies_watched:
    print(f"I've haven't watched that yet!")


number = 7

user_input = input("Enter 'y' if you would like to play! ").lower()

if user_input == 'y':
    user_number = int(input('Guess our number: '))
    if user_number == number:
        print('You guessed correctly! ')
    elif abs(number - user_number) == 1:
        print("you were off by one.")

    else:
        print('Sorry, it is wrong!')
