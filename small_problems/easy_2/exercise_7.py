# Exclusive Or

# The or operator returns a truthy value if either or both of its 
# operands are truthy, a falsy value if both operands are falsy. 
# The and operator returns a truthy value if both of its operands 
# are truthy, and a falsy value if either operand is falsy. This 
# works great until you need only one of two conditions to be 
# truthy, the so-called exclusive or, also known as xor 
# (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two 
# arguments, and returns True if exactly one of its arguments is 
# truthy, False otherwise.

# input:
#   2 arguments
# output:
#   True if 1 argument is True
#   False if both are True or False

# function takes 2 arguments
# returns True if only 1 argument is True

# example
# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# data structure
# list comprehension
# empty list to contain truthy values

# algorithm
# empty list variable
# to append truthy values to list
# if list length is 1
# return True
# else
# return False

def xor(value1, value2):
    values = (value1, value2)
    truthy_values = [value 
                     for value in values
                     if value]
    
    return len(truthy_values) == 1


# solution by LSBot
# def xor(value1, value2):
#     return bool(value1) != bool(value2)
# Does the xor function perform short-circuit evaluation of its operands? 
# No, it needs to evaluate both expressions
# Does short-circuit evaluation in xor operations even make sense?
# No, in this case, xor needs to evaluate both expressions
# and return True if only one evaluates to truthy