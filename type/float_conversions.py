# Type Conversions

import math

# float() function
float_str = "3.14"
float_number = float(float_str)
print(float_number) # Output: 3.14

# ValueError
input = 'abc'
try:
	result = float(input)
except ValueError:
	print("Cannot convert value to float")
                
# TypeError for any other data type
float_input = {'value': 42}
try:
    result = float(float_input)
except TypeError:
    print("Invalid input type for conversion")

# Not-a-Number (nan)
result = float('inf') - float('inf')
print(result)       # output: nan

# float handles 'NaN' differently
nan_string = "NaN"
# This is just a string with the characters N-a-N
nan_float = float(nan_string)
# Converting the string to a float value
print(nan_float)    # output: nan

# equality operators can't be use with nan values
print(nan_float == nan_float)
# output: False

# to check if something is NaN 
print(math.isnan(nan_float))
# output: True