# Write a function called count_characters that takes a 
# string as input and returns a dictionary where the keys 
# are the characters in the string and the values are the 
# number of times each character appears. Spaces should be 
# ignored.

def clean_text(text):
    cleaned = ''
    
    for char in text:
        if char.isalpha():
            cleaned += char.lower()

    return cleaned

def count_characters(message):
    letters = {}
    cleaned_message = clean_text(message)
    
    for char in cleaned_message:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    
    return letters
            
print(count_characters("hello world"))
# Returns {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# revised solution:
# def count_characters(message):
#     letters = {}
    
#     for char in message:
#         if char.isalpha():  # Only count alphabetic characters
#             char = char.lower()  # Case insensitive counting
#             letters[char] = letters.get(char, 0) + 1
    
#     return letters