# Logical Operators

# and operator
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

num = 5
print((num < 10) and (num > 3))     # True
print((num < 10) and (num > 6))     # False
print((num > 10) and (num < 6))     # False
print((num > 10) and (num < 3))     # False

# note: always a good practice to use  
# parentheses with expressions that involve
# multiple operators

#e.g ((n < 10) and (num > 3))

# chain as many expressions as you like with 
# the 'and' operator 

num = 5
print((num < 10) and (num > 0) and ((num % 2) == 1))    # True
print((num < 10) and (num > 0) and ((num % 2) == 1) and False)      # False


# 'or' operator
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

num = 5
print((num < 10) or (num > 3))      # True
print((num < 10) or (num > 6))      # True
print((num > 10) or (num < 6))      # True
print((num > 10) or (num < 3))      # False


# 'not' operator
# not serves as a logical negation

print(not True)     # False
print(not False)    # True

value = 3
is_even = (value % 2 == 0)

print(is_even)      # False
print(not is_even)  # True


# short-circuit operators
# both 'and' & 'or' operators perform
# short-circuit operations

print(False and len(None))  # False

# print(True and len(None))   
# TypeError: object of type 'NoneType' has no len()

print(True or len(None))    # True


# real-life example of short-circuit 
# if name != None and name.isupper():
#     print(f"Hi, {name}.")
# else:
#     print("Hello, whoever you are.")

