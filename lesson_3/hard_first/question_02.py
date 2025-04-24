# Question 2

# What does the last line in the following 
# code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)     # [1, 2]
print(dictionary)   # {'first': [1, 2]}

# Try to answer without running the code or looking at the solution.

# in line 7: the dictionary['first'] is assigned to num_list
# meaning they are both referencing the same object
# so when num_list.append(2) is invoked, it mutates the list
# so when you print num_list - [1, 2]
# but when you print dictionary - {'first': [1, 2]}

# LS:
# Instead of modifying the original list,
# What if we wanted to modify just the num_list

# method 1:
# We can initialize num_list with a reference to a copy of the 
# original list
dictionary = {'first': [1]}
num_list = dictionary['first'].copy()
num_list.append(2)

print(num_list)
print(dictionary)

# method 2:
# We can use list slicing which returns a new list
# using slicing methods returns shallow copy of the list
dictionary = {'first': [1]}
num_list = dictionary['first'][:]
num_list.append(2)

print(num_list)
print(dictionary)