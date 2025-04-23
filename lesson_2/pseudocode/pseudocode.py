# pseudocode

# pseudocode for function that determines wihch number in a collection has the greatest value

# given a collection of numbers
#   iterate through the collection one by one
#       save the first value as the starting value
#       for each iteration, compare the saved value with the current value
#           if the current number is greater
#               reassign the saved number as the current value
#           otherwise if the current value smaller or
#           move to the next value in the collection
# after iterating through the collection, return the saved value

# Keyword   Meaning
# START     start of the program
# SET       set a variable that we can use for later
# GET       retrieve input from user
# PRINT     display output to user
# READ      retrieve value from a variable
# IF/ELSE
# IF/ELSE   show conditional branches in logic
# WHILE     show looping logic
# END       end of the program

# START

# Given a collection of integers called numbers

# SET iterator = 1
# saved_number = value within numbers collection at space 1

# WHILE iterator <= length of numbers
    # SET current_number = value within numbers
    # IF current_number > saved_number
    #   saved_number = current_number
    # iterator = iterator + 1
# PRINT saved_number

def greatest_number(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number
    
        iterator += 1
    
    return saved_number

numbers = [100, 2, 3, 10, 15]
print(greatest_number(numbers))