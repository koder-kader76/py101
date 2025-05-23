# UTF-16 String Value

# Write a function that determines and returns the UTF-16 string
# value of a string passed in as an argument. The UTF-16 string
# value is the sum of the UTF-16 values of every character in the
# string. (You may use ord to determine the UTF-16 value of a
# character.)

# These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# Solution 1:
def utf16_value(str_param):
    total_sum = 0

    for char in str_param:
        total_sum += ord(char)

    return total_sum

# Solution 2:
def utf16_value(str_param):
    utf16_values = [ord(char)
                    for char in str_param]

    return sum(utf16_values)

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)