# 9. Clean up the words

# Given a string that consists of some words and an assortment of 
# non-alphabetic characters, write a function that returns that 
# string with all of the non-alphabetic characters replaced by 
# spaces. If one or more non-alphabetic characters occur in a 
# row, you should only have one space in the result (i.e., the 
# result string should never have consecutive spaces).

def is_ascii_letter(char):
    return char.isalpha() and char.isascii()

def clean_up(random_text):
    cleaned_text = ''
    
    for char in random_text:
        if not is_ascii_letter(char):
            if not cleaned_text.endswith(' '):
                cleaned_text += ' '
        else:
            cleaned_text += char
    
    return cleaned_text

# solution by LSBot using isascii()
# def clean_up(random_text):
#     cleaned_text = ''
    
#     for char in random_text:
#         if char.isalpha() and char.isascii():  # Only allow ASCII letters
#             cleaned_text += char
#         elif not cleaned_text.endswith(' '):
#             cleaned_text += ' '
    
#     return cleaned_text

def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        if char.isalpha():
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text

print(clean_up("---what's my +*& line?") == " what s my line ")
# True
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")  # True
print(clean_up('') == '')