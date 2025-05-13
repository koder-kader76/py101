# Create a function that takes a list of integers and 
# returns a new list containing only unique elements from 
# the original list, while preserving the original order.

def unique_elements(numbers):
    unique = []
    
    for number in numbers:
        if number not in unique:
            unique.append(number)
    
    return unique