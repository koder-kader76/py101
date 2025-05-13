# Write a function that takes a string and returns that 
# string with all vowels removed.

def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    text_sequence = [
        char 
        for char in word 
        if char.lower() not in vowels
    ]

    return ''.join(text_sequence)

print(remove_vowels("hello") == "hll")  # True
print(remove_vowels("python") == "pythn")  # True
print(remove_vowels("aeiou") == "")  # True