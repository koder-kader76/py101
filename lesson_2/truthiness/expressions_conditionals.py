# in real code, True or False values aren't 
# used - the expressions are evaluated to
# truthy or falsy

# e.g
num = 5

if num < 10:
    print("small number")
else:
    print("large number")

# e.g Python REPL
num = 5
print(num < 10)     # True

num = 12
print(num < 10)     # False

# functions don't return True or False 
# explicitly
# returns the result of a conditional
# expression

def is_small(number):
    return number < 10

num = 15

if is_small(num):
    print("small number")
else:
    print("large number")
# large number

