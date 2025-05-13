# Write a function that compares two lists of numbers and 
# returns True if all elements in the first list are 
# greater than their corresponding elements in the second 
# list.

def all_greater(list1, list2):
    
    index = 0

    while index < len(list1):
        if not (list1[index] > list2[index]):
            return False
        
        index += 1

    return True

# Test cases
print(all_greater([10, 20, 30], [5, 15, 25]))  # Should return True
print(all_greater([10, 20, 30], [5, 25, 20]))  # Should return False