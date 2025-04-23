# Question 2

# How can you determine whether a given string ends with an
# exclamation mark (!)? Write some code that prints True or False
# depending on whether the string ends with an exclamation mark.

# Example
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def ends_with_exclamation(sentence):
    # return sentence[-1] == '!'
    return sentence.endswith('!')

print(ends_with_exclamation(str1))
print(ends_with_exclamation(str2))

# LS:
# print(str1.endswith("!"))  # True
# print(str2.endswith("!"))  # False