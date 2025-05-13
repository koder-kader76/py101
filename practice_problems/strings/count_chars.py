# Create a function that counts the occurrences of each 
# character in a string and returns a dictionary with the 
# results.

def count_chars(message):
    characters = {}
    
    for char in message:
        characters[char] = characters.get(char, 0) + 1
    
    return characters

print(count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1})  # True
print(count_chars("python!") == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})  # True