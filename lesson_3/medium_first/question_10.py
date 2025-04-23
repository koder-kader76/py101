# Question 10

# In Python, every object has a unique identifier that can be 
# accessed using the id() function. This function returns the 
# identity of an object, which is guaranteed to be unique for the 
# object's lifetime. For certain basic immutable data types like 
# short strings or integers, Python might reuse the memory 
# address for objects with the same value. This is known as 
# "interning".

# Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# output: True
# For Python, interning includes integers from -5 to 256
# the assignment for a and b may be different but as interning is involved, both a and b with reference the same object in memory
# so the expression will evaluate to True

# LS:
# The output is True.

# Here, a and c reference the same object in memory, so their ids are the same. b will, in this case, have the same id as a and c due to interning. Therefore, the code will output True.