# Create a function that takes a list of integers as an 
# argument and returns a list of lists, where each inner 
# list contains elements from the original list that, when 
# summed, equal the target sum of 10. Each element can 
# only be used once.

def find_combinations_with_sum_10(numbers):
    if not numbers: 
        return []

    pairs = []

    while len(numbers):
        number = numbers.pop(0)
        index = 0
        while index < len(numbers):
            if sum([number, numbers[index]]) == 10:
                pairs.append([number, numbers[index]])
                numbers.pop(index)
                break
            index += 1
    return pairs