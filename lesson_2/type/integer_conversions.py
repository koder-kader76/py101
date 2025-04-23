# Type Conversions

# int() function
integer_str = '42'
integer = int(integer_str)
print(integer)  # 42

# converting a non numeric value to integer
non_numeric_value = 'abc'
try:
    non_numeric_integer = int(non_numeric_value)
except ValueError:
    print("Cannot convert to int")
# Cannot convert to int

# int() function can accept floating point numbers
floating_point_numeric = 10.00
integer_floating = int(floating_point_numeric)
print(integer_floating) # 10

# bytes-like object (not discussed)

# Boolen values
true_value = True
false_value = False
integer_true = int(true_value)
integer_false = int(false_value)
print(integer_true, integer_false)  
# Output: 1 0

# raises TypeError for e.g list input
input_value = ['42']
try:
    numeric_value = int(input_value)
except TypeError:
    print("Invalid input type for conversion")
# Output: Invalid input type for conversion