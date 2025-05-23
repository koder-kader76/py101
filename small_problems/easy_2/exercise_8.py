# Odd Lists
# Write a function that
# returns a list that contains every other element of a list that is passed in as an argument.
# The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

# empty lists as argument - return empty list
# return every item in index modulo 2


# example
# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# data structure
# input: list item
# output: list item


# solution using list comprehensions
def oddities(values):
    oddity = [
        value
        for value in values
        if values.index(value) % 2 == 0
    ]

    return oddity

# solution using list slicing
def oddities(values):
    oddity = []
    index = 0

    while index < len(values):
        if index % 2 == 0:
            oddity += values[index : index + 1]
        index += 1

    return oddity

# solution by LSBot 
def oddities(values):
    return values[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True