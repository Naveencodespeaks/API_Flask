import math
numbers = [1,3,5]
double = [num * 2 for num in numbers]
print(double)




import math  # Import the math module to access the sqrt function

given_numbers = [2, 4, 5, 67, 54, 3]

square_root = [math.sqrt(number) for number in given_numbers]

print(square_root)


friends = ['Rolf', 'sam', 'samantha', 'jon']

starts_s = []

for friend in friends:
    if friend.startswith('s'):
        starts_s.append(friend)

print(starts_s)


starts_s = [friend for friend in friends if friend.startswith('s')]

print(friends[0] is starts_s)

print("Friends", id(friends),"starts:", id(starts_s))