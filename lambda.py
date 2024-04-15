def add(x,y):
    return x+ y
print(add(5,7))


add = lambda x,y : x + y

print(add(20,7))

print(add(44,77))

print(lambda x,y : x + y)(50,79)

def double(x):
    return x *2 

sequence = [1,2,3,4,5,6,8]
doubled = [double(x) for x in sequence]
doubled = map(double,sequence)
