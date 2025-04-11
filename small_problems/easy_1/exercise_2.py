# Odd Numbers

# Print all odd numbers from 1 to 99, 
# inclusive, with each number on a separate 
# line.

# PEDAC
# Input - numbers from 1 to 99
# output - print only odd numbers from 1 - 99
# Requirements
#   collection of numbers from 1 - 99 - not including 0
#   print only the odd numbers
# Rules
#   function should print odd numbers on a separate line
#   only odd numbers - even numbers should be passed
#   numbers should not start with 0 and should end at 99
# Mental model:
#   a function should iterate over the numbers 1 - 99 and print out all the odd numbers, each number on on individual line

# Example
# odd_numbers(collection)
# 1
# 3
# 5
# 7

# Data Structure
# create a list of numbers from 1 - 99 using the range object
# iterate over the numbers using a for loop

# Algorithm
# create a list(range(1, 100))
# iterate over the list
# print only dd numbers using % operator
# end the iteration when number is 99

def odd_numbers():
    numbers = list(range(1, 100))

    for number in numbers:
        if number % 2 == 1:
            print(number)

odd_numbers()

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# using the algorithm, change numbers variable
# to be assigned with list(range(1, 100, 2))

def odd_numbers2():
    numbers = list(range(1, 100, 2))

    for number in numbers:
        print(number)

odd_numbers2()