# 12. Always Return Negative

# Write a function that takes a number as an argument. If the 
# argument is a positive number, return the negative of that 
# number. If the argument is a negative number, return it as-is.

def negative(number):

    if number > 0:
        return number * -1
    else:
        return number

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)      # True


# LS:
def negative(number):
    return -abs(number)

# Python has a built-in abs function which returns the absolute 
# value of the specified number. By prefixing the result of abs
# (number) with a negative sign -, the function effectively 
# always returns the negative representation of the given number.