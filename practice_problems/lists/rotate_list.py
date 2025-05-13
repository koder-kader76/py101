# Write a function that rotates the elements of a list by 
# n positions. If n is positive, rotate to the right. If n 
# is negative, rotate to the left.

def rotate_list(numbers, nth):
    if not numbers:
        return []
    
    results = numbers[:]
    length = len(results)

    if length > 0:
        positions = nth % length if length else 0
    
    if positions > 0:
        results = results[-positions:] + results[:-positions]
    elif positions < 0:
        results = results[:-positions] + results[-positions:]

    return results