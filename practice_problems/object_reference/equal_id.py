a = 42
b = 42
c = a

print(id(a) == id(b))
print(id(a) == id(c))

# What will be printed to the console in this example?

# The first print call is supposed to print False. Both a and b are assigned to the value 42 but these 2 are distinct objects. But due to interning, Python will output True for the first print call.
# The second print call will output True. c is assigned to the variable reference a which means these 2 variables are referencing the same object in memory.
# This concept demonstrates variables are pointers to objects in memory and multiple variables can reference the same object in memory. It also highlights interning concept as Python tries to save memory space.