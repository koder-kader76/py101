# Question 4

# Ben was tasked to write a simple Python function to determine 
# whether an input string is an IP address using 4 dot-separated 
# numbers, e.g., 10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number. It 
# determines whether a string is a numeric string between 0 and 
# 255 as required for IP numbers and asked Ben to use it. Here's 
# the code that Ben wrote:

# Alyssa reviewed Ben's code and said, "It's a good start, but 
# you missed a few things. You're not returning a false 
# condition, and you're not handling the case when the input 
# string has more or less than 4 components, 
# e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.

def is_an_ip_number(component):
    if component.isdigit():
        number = int(component)
        return 0 <= number <= 255
    return False

# added a separate function to check length of list
def is_valid_ip(separated_list):
    return len(separated_list) == 4

def is_dot_separated_ip_address(input_string):
    # guard clause against empty string
    if not input_string:
        return False

    dot_separated_words = input_string.split(".")

    # guard clause to check if length if 4
    if not is_valid_ip(dot_separated_words):
        return False

    # changed the while loop into a for loop
    # instead of break, return False 
    # if string is not an ip number
    for word in dot_separated_words:
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address("10.4.5.11"))
print(is_dot_separated_ip_address("4.5.5"))
print(is_dot_separated_ip_address(""))

# Input: 
#   Ip address 10.4.5.11
# Output: 
#   True if valid ip
#   False is invalid ip

# valid ip address - ipv4 address 
# string.split() - return list with 4 elements
# all strings should be numeric value from 0 to 255

# Example
# print(is_dot_separated_ip_address("10.4.5.11"))   # True
# print(is_dot_separated_ip_address("4.5.5"))       # False
# print(is_dot_separated_ip_address("1.2.3.4.5"))   # False

# Current output:   4.5.5 - True

# data structure : 
    # function to test if list has exactly 4 elements

# LS:
# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) != 4:
#         return False

#     while dot_separated_words:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             return False

#     return True