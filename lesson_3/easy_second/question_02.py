# Question 2

# Given a number and a list, determine whether the number is included in the list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

def number_in_list(numbers_, number):
    return number in numbers_

print(number_in_list(numbers, number1))
print(number_in_list(numbers, number2))