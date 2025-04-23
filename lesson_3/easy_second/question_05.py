# Question 5

# How would you verify whether the data structures assigned to 
# the variables numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)    # True
print(type(table) is list)      # False

# LS:
# isinstance(numbers, list)  # True
# isinstance(table, list)    # False