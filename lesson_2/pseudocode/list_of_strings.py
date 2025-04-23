# pseudocode 

# a function that takes a list of strings, and returns a string that is all those strings concatenated together 

# START

# given a list of strings - returns one long string of all the strings concatenated together

# SET final_string = ''

# FOR string in strings:
#   final_string = final_string + string

# PRINT final_string

def combined_texts(list_of_text):
    final_text = ''

    for text in list_of_text:
        final_text += text
    
    return final_text


text_list1 = ['the', 'dog', 'came', 'home']
text_list2 = ['monty', 'python']
text_list3 = ['']

print(combined_texts(text_list1))
print(combined_texts(text_list2))
print(combined_texts(text_list3))