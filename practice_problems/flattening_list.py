# Advanced​: Implement a function that flattens a nested 
# list structure. The function should take a list that 
# might contain other lists as elements and return a 
# single flat list with all elements.

def has_nested_lists(input_numbers):
    for number in input_numbers:
        if isinstance(number, list):
            return True
    
    return False


def flatten_list(input_list):
    if not input_list:
        return []

    numbers = input_list.copy()
    
    while has_nested_lists(numbers):
        for number in numbers:
            if isinstance(number, list):
                index = numbers.index(number)
                num = numbers.pop(index)
                numbers.extend(num)
    
    return numbers


print(flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6])
print(flatten_list([1, 2, 3]) == [1, 2, 3])
print(flatten_list([[1, 2], [3, 4], []]) == [1, 2, 3, 4])
print(flatten_list([]) == [])