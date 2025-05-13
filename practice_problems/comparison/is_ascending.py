def is_ascending(numbers):
    index = 0

    if len(numbers) <= 1:
        return True
    
    while index < len(numbers) - 1:
        if numbers[index] > numbers[index + 1]:
            return False
        index += 1
        
    return True


# Test cases
print(is_ascending([1, 2, 3, 4]))  # True
print(is_ascending([1, 2, 2, 3]))  # True
print(is_ascending([4, 3, 2, 1]))  # False