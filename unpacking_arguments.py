def multiply(*args):
    print(args)
    for arg  in args:
        total = total * arg
    return total

multiply(1,3,5)


def add(x,y):
    return x + y

nums = [10,59]
alpha = add(*nums)

print("Here we are printing the following functions as the additions")
print(alpha)


def mul(x,y):
    return x * y

nums = (19,30)

print("Here we are printing the following multipication and as the function")
print(mul(*nums))


def add1(x,y):
    return x + y

nums = {'x':18, 'y': 20}
print(add(**nums))


def add2(x,y):
    return x+y

nums = {"x": 30, "y": 50}
print(add2(**nums))


def mul(*args):
    total = 1
    for arg in args:
        total = total * arg

    
    return total

def apply(*args, operator):
    if operator == "*":
        return mul(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator to apply()."
    
print(apply(1,3,6,7, operator="+"))


def both(*arg, **kwargs):
    print(arg)
    print(kwargs)

print(both(1,2,3,4, name = "bob", age = '20'))
