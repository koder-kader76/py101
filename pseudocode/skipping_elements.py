# pseudocode practice problem

# a function that takes a list of integers, and returns a new list with every other element from the original list, starting with the first element.

# START

# DEF skipping_elements(list)
#   SET new_list = []
#   SET index = 0

#   WHILE index < len(list):
#       SET new_list add list[index]
#       SET index = index + 2

#   PRINT new_list

def every_other(numbers):
    new_numbers = []
    index = 0

    while index < len(numbers):
        new_numbers.append(numbers[index])

        index += 2
    
    return new_numbers

num1 = [1, 4, 7, 2, 5]
num2 = [1, 4, 7, 2, 5, 6, 8]
num3 = [1, 4, 7, 2, 5, 6, 8, 9, 10, 11]

print(every_other(num1))
print(every_other(num2))
print(every_other(num3))