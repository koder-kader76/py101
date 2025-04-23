# pseudocode practice

# a function that determines the index of the 3rd occurrence of a given character in a string. For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None. 

# START

# given a character and a string, function should return the index where the character is repeated the 3rd time
# should return None if character is not repeated 3 times

#   SET index = 0
#   SET char_index = []

#   WHILE index < len(string):
#       IF string[index] == char:
#           char_index add index
#       index += 1
#   
#   IF length(char_index < 3):
#       PRINT None
#   ElSE
#       PRINT char_index[2]

def third_occurence(char, text):
    index = 0
    char_index = []

    while index < len(text):
        if text[index] == char:
            char_index.append(index)

            if len(char_index) == 3:
                break

        index += 1

    if len(char_index) < 3:
        return None
    
    return char_index[2]

print(third_occurence('e', 'axbxcdxex'))