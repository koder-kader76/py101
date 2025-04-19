# Squaring an Argument

# Using the multiply function from the "Multiplying Two Numbers"
# exercise,
# write a function that computes the square of its argument
# (the square is the result of multiplying a number by itself).

def multiply(number1, number2):
    return number1 * number2

def square(number, nth):
    # handling edge cases for 0, 1
    if nth == 0:
        return 1

    if nth == 1:
        return number

    # further exploration
    exponential_number = number
    for i in range(1, nth):
        exponential_number = (multiply
                             (exponential_number, number))
    
    return exponential_number

print(square(5, 1))



# Solution provided by LSBot
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    
    # if exponent is even
    if exponent % 2 == 0:
        half_power = power(base, exponent // 2)
        return multiply(half_power, half_power)
    else:
        half_power = power(base, 
                           (exponent - 1) // 2)
        return multiply(base, 
                        multiply(half_power, 
                                 half_power))

print(power(10, 9)) # 1000000000
