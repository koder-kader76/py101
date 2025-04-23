# Question 5

# Starting with the string:

# print the string with the case of all letters swapped:
# "tHE mUNSTERS ARE CREEPY AND SPOOKY."

# That is, lowercase letters are converted to uppercase, and 
# uppercase letters are converted to lowercase"

munsters_description = "The Munsters are creepy and spooky."

# function takes a sentence and returns a string where
# each character case is reversed non-character case is returned 
# as is
def switch_case(phrase):
    if not isinstance(phrase, str):
        return "Error: input must be string"
    
    inverted_phrase = ''

    for char in phrase:
        if char.isalpha():
            if char.islower():
                inverted_phrase += char.upper()
            else:
                inverted_phrase += char.lower()
        else:
            inverted_phrase += char

    return inverted_phrase



print(switch_case(munsters_description.title()))
# tHE mUNSTERS ARE CREEPY AND SPOOKY.

print(switch_case("Forums use Github flavored markdown"))
# fORUMS USE gITHUB FLAVORED MARKDOWN

sentence = (
"""That is, lowerCase Letters Are Converted to uppercase, and uppercase letters are converted to lowercase"""
)

print(switch_case(sentence.title()))
print(switch_case(2334))


# LS:
# print(munsters_description.swapcase())