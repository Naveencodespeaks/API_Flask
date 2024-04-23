def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0 ")
        
    return dividend / divisor


grade = []
print("Welcome to the average calculator. ")
try:
    average = divide(sum(grade),len(grade))
    print(f"The average grade is {average}")
    
except ZeroDivisionError as e :
    print("These are no grades yet in your list. ")   
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you")




