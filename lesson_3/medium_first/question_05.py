# Question 5

# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))    # False

# when string "nan" is coerced into a float, it becomes a special
# number NaN - Not-a-Number
# the output will return False as you can't use equality operators on nan - it behaves differently

# Bonus question
# How can you reliably test if a value is nan?

# import math 
# use math.isnan() function to check if value is nan
import math

nan_value = float("nan")

print(nan_value == float("nan"))    # False

print(math.isnan(nan_value))    # True