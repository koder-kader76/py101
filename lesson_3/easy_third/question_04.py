# Question 4

# What will the following code output?

my_list1 = [
    {"first": "value1"}, 
    {"second": "value2"}, 
    3, 
    4, 
    5,
]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# Try to answer without running the code.
# line 5 - initialize a my_list1 with a list
# line 12 - my_list2 initialized with my_list1.copy()
# list.copy() makes a shallow copy of the original list
# my_list2 is referencing a different list object but the same nested dictionary as my_list1
# line 13; when my_list2 is reassigned, it mutates the dictionary object and the value for 'first' is now 42
# since my_list1 is referencing the same nested dictionary as my_list2, it will point the mutated dictionary
# so when you print my_list1 
# my_list1 = [{"first": 42}, {"second": "value2"}, 3, 4, 5]
