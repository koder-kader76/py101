# 1. Isn't it Odd?

# Write a function that takes one integer 
# argument and returns True when the number's 
# absolute value is odd, False otherwise.

# PEDAC
# Input / Output
#   Integer / True/False
# Requirements
#   argument must be integer
#   no floats / strings / any other type
# Rules 
#   function takes 1 arugment (integer)
#   check integer's absolute value - positive 
#   integer
#   function can take negative numbers
# Mental model
#   write a function that takes a number
#   returns True if number is odd 
#   otherwise False

# Example / Test Cases
#   is_odd(10)      - False
#   is_odd(11)      - True
#   is_odd(0)       - False
#   is_odd(-101)    - True

# Data Structure
#   function returns boolean value
#   return True or False

# Algorithm
# is_odd(number):
# determine absolute value
# if absolute value is positive
# else absolute value multiply by -1
# return boolean value

def is_odd(number):
    
    if number >= 0:
        absolute = number
    else:
        absolute = number * -1
    
    return absolute % 2 != 0

print(is_odd(10))     # False
print(is_odd(11))     # True
print(is_odd(0))      # False
print(is_odd(-101))   # True