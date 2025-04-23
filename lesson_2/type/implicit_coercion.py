# Implicit Coercion

# operation with integer & float
x = 3
y = 2.0
result = x + y
print(result)   # 5.0
print(type(result)) 

# concatenation with string & non-string
name = "John"
age = 35
try:
    print(name + age)
except TypeError:
    print("TypeError: can only concatenate str (not \"int\") to str")
# TypeError: can only concatenate str (not "int") to str

# print() converts non-string values to string objects
name = "John"
age = 35
print(name, age)
# John 35