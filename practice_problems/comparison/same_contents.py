def lists_have_same_contents(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return False
    
    if not list1 and not list2:
        return True

    set1 = set(list1)
    set2 = set(list2)

    return set1 == set2
        
# Test cases
print(lists_have_same_contents([1, 2, 3], [3, 2, 1]))  
# True
print(lists_have_same_contents([1, 2, 3], [1, 2, 3, 4]))  # False