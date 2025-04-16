# Sum or Product of Consecutive Integers

# Write a program that asks the user to enter 
# an integer greater than 0, then asks
# whether the user wants to determine the sum
# or the product of all numbers between 1 and
# the entered integer, inclusive.

# example 1
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s
# The sum of the integers between 1 and 5 is 15.

# example 2
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p
# The product of the integers between 1 and 6 is 720.

# PEDAC
# Process the problem
# Ask user for number N greater than 0
# Ask the user if they want the sum or product
# from numbers 1 to N inclusive

# rules
# number must be greater than zero
# number can be 1
# number cannot be negative or float or any other type 
# string input to be coerced into integer
# also ask for input 's' or 'p'
# only s & p will recognized
# input validation on 2 occasions for number & str

# example
# 5 & s = 1 + 2 + 3 + 4 + 5 --> 15
# 6 & p = 1 * 2 * 3 * 4 * 5 * 6 --> 720

# Data Structure
# list(range(1, N + 1))
# user input 5: list(range(1, 6))
# [1, 2, 3, 4, 5]
# user input - try/except ValueError

# Algorithm
# ask user for input
#   if input invalid - input() again
#   print the value
# ask user for operation
#   if input invalid - ask again()
#   print the value
# compute the sum / product of n numbers
# print the result

def integer_input():
    print("Please enter an integer greater than 0: ", 
          end='')
    str_input = input()
    
    while True:
        try:
            if int(str_input) > 0:
                return int(str_input)
            else:
                print("Integer should be greater than 0: ",
                      end='')
                str_input = input()
        except ValueError:
            print("Please enter a valid integer: ", 
                  end='')
            str_input = input()
    
def compute():
    
    print("Enter 's' to compute the sum, or 'p'"
          "to compute the product. ", end='')
    str_compute = input()

    while True:
        if str_compute in ['s', 'p']:
            return str_compute
        print("Please enter 's' or 'p'", 
              end='')
        str_compute = input()

def operation(num, ops):
    numbers = list(range(1, num + 1))
    if ops == 's':
        sum_total = sum(numbers)
        print(f"The sum of the integers between 1 "
              f"and {num} is {sum_total}.")
    else:
        product_total = 1
        for number in numbers:
            product_total *= number
        print(f"The product of the integers between 1 "
              f"and {number} is {product_total}.")


def main():
    input_num = integer_input()
    input_ops = compute()
    operation(input_num, input_ops)

main()