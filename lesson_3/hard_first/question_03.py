# Question 3

# Given the following similar sets of code, what will each code snippet print?

# A)

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
# "one is: ["one"]"
print(f"two is: {two}")
# "two is: ["two"]"
print(f"three is: {three}")
# "three is: ["three"]"

# In this code, all three variables are re-assigned within
# the function which makes them lolcal variables 
# they can only be accessed within the function 
# since they are local variables, they cannot be accessed
# outside of the function, the variables one, two & three
# will still reference the same values

# B) 

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
# "one is: ["one"]"
print(f"two is: {two}")
# "two is: ["two"]"
print(f"three is: {three}")
# "three is: ["three"]"

# This code works the same way as example A
# the variables inside the function cannot be accessed
# outside of the function once there is assignment
# which makes them local variables
# So one, two & three will still reference the same values

# C)

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
# "one is: ["two"]"
print(f"two is: {two}")
# "two is: ["three"]"
print(f"three is: {three}")
# "three is: ["one"]"

# In this code the variables are passed in as a reference
# since the objects are mutable, this code will perform 
# mutation on all the objects passed into the function
# so in this instance, the objects being referenced are mutated


# LS:
# In all three scenarios, the variables one, two, and three 
# inside the mess_with_vars function are local to the function. 
# They are not the same as the variables one, two, and three 
# defined outside the function. This is known as variable 
# shadowing, where the local variables inside the function 
# overshadow the variables outside the function with the same 
# names.

# A)
# The output is:
    # one is: ['one']
    # two is: ['two']
    # three is: ['three']

# Since variables one, two, and three in the mess_with_vars 
# function are local, reassigning them does not affect the 
# original lists.

# B)
# The output is:
    # one is: ['one']
    # two is: ['two']
    # three is: ['three']

# Again, the local variables in the mess_with_vars function are 
# being reassigned, but this doesn't change the original lists.

# C)
# The output is:
    # one is: ['two']
    # two is: ['three']
    # three is: ['one']

# In this case, the mess_with_vars function modifies the content 
# of the lists directly. Since lists in Python are mutable and 
# passed by object reference, the changes are reflected outside 
# the function.