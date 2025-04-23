# pseudocode practice

# a function that takes two lists of numbers and returns the result of merging the lists. The elements of the first list should become the elements at the even indexes of the returned list, while the elements of the second list should become the elements at the odd indexes.

# START

# function takes 2 lists and merges them
# elements of first list should be added in the even indexes
# elements of the second list should be added in the odd indexes

# SET merged_list = []
# SET index = 0

# WHILE length(list1) or length(list2):
#   merged_list add list1.pop(index)
#   merged_list add list2.pop(index)

# PRINT merged_list

def merge(list1, list2):
    
    merged_list = []
    index = 0

    while len(list1) or len(list2):
        merged_list.append(list1.pop(index))
        merged_list.append(list2.pop(index))
    
    return merged_list

print(merge([3, 6, 9], [5, 10, 15]))