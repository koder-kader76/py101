# Implement a function that finds the maximum value in a 
# nested list structure without using Python's built-in max
# () function.

def flatten_list(input_list):
    result = []

    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    
    return result

def find_max_nested(nested_list):
    if not nested_list:
        return None
    
    max_number = float('-inf')
    numbers = flatten_list(nested_list)

    for number in numbers:
        if number > max_number:
            max_number = number
    
    return max_number

# Test cases
print(find_max_nested([1, [2, 3], [[4], 5]]))  # Should return 5
print(find_max_nested([[10, 2], [3, [8, 9]], 1]))  # Should return 10