# 10 What Century is That?

# Write a function that takes a year as input and returns the 
# century. The return value should be a string that begins with 
# the century number, and ends with 'st', 'nd', 'rd', or 'th' as 
# appropriate for that number.

# New centuries begin in years that end with 01. So, the years 
# 1901 - 2000 comprise the 20th century.

import math

def century(year):
    dictionary = {
        'st': ['01', '21', '31', '41', '51', '61', '71', '81', '91'],
        'nd': ['02', '22', '32', '42', '52', '62', '72', '82', '92'],
        'rd': ['03', '23', '33', '43', '53', '63', '73', '83', '93']
    }

    rounded_number = str(math.ceil(year / 100))

    if len(rounded_number) == 1:
        rounded = '0' + rounded_number
    else:
        rounded = rounded_number[-2:]

    dict_key = [key 
                for key, value in dictionary.items()
                if rounded in value]

    if dict_key:
        return rounded_number + dict_key[0]
    else:
        return rounded_number + 'th'


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True