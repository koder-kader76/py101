# Floating Point Arithmetic

# Write a program that prompts the user for two positive numbers
# (floating-point),
# then prints the results of the following
# operations on those two numbers:
    # addition
    # subtraction
    # product
    # quotient
    # floor quotient
    # remainder
    # power
# Do not worry about validating the input

# input: 2 floating-point numbers
# output:
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

# code takes string input
# coerces into floating-point numbers
# prints out value for each operation
# no input validation required
# custom prompt function

# edge cases: 2nd number cannot be zero
#           : numbers can be negative

# data structure: floating point numbers
#               : output string of operations

# algorithm:
# get input from user
# return output

def prompt(message=''):
    return f"==> {message}"

def get_number_from_user(request):
    number_from_user = input(request)
    return float(number_from_user)

def first_second_numbers():

    first_number = get_number_from_user(
                        prompt("Enter the first number: "))

    while True:
        second_number = get_number_from_user(
                        prompt("Enter the second number: "))
        if second_number != 0:
            break
    
    return [first_number, second_number]

def addition(first, second):
    return first + second

def subtraction(first, second):
    return first - second

def product(first, second):
    return first *  second

def quotient(first, second):
    return first / second

def floor_quotient(first, second):
    return first // second

def remainder(first, second):
    return first % second

def power(first, second):
    return first**second

def ops_string(first, second, operator, operation):
    return (f"{first} {operator} {second} = "
            f"{operation(first, second)}")

def operations():
    first, second = first_second_numbers()

    ops_list = [
        ('+', addition),
        ('-', subtraction),
        ('*', product),
        ('/', quotient),
        ('//', floor_quotient),
        ('%', remainder),
        ('**', power),
    ]

    for ops in ops_list:
        print(prompt(ops_string(first, second, ops[0], ops[1])))
           
operations()