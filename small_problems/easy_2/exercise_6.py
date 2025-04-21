# The End Is Near But Not Here

# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

# input: string argument
# output: return penultimate word
# assume all arguments will be non-blank characters
# input string will always have 2 words or more

# example
# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# data structure: input string -> list

# algorithm
# convert string to list
# pop() 2 x to retrieve 2nd last item

def penultimate(string):
    words_list = string.split()
    # checking if string has empty string or 1 word
    if len(words_list) == 1:
        return words_list[0]
    elif len(words_list) > 1:
        return words_list[-2]
    else:
        return "Empty string"

def middle_word(string):
    words_list = string.split()
    # checking if string has empty string or 1 word
    if len(words_list) == 1:
        return words_list[0]
    elif len(words_list) > 1:
        index = len(words_list) // 2
        return words_list[index]
    else:
        return "Empty String"
        

print(middle_word("Launch School is great!"))
print(middle_word("argument"))
