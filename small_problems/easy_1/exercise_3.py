# Even Numbers

# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# PEDAC
# print all even numbers from range 1 .. 99
# print each number on separate line
# all numbers printed must be even
# iteration should continue over odd numbers

# example
# range(1, 100) # 2, 4, 6, ...96, 98

# data structure
# loop over range object
# if statement with modulo operator

# algorithm
# numbers = list(range(1, 100))
# iterate over numbers
# print out all even numbers

numbers = list(range(1, 100))
# print(numbers)

for number in numbers:
    if number % 2 == 0:
        print(number)

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# data structure - list(range(2, 100, 2))
numbers = list(range(2, 100, 2))
# print(numbers)

for number in numbers:
    print(number)