# Create a function that takes a sentence as input and 
# returns a new string where every word is capitalized.

def capitalize_words(message):
    if not message:
        return ''
    
    words = message.split()
    capitalized_words = [word.capitalize() for word in words]
    
    return ' '.join(capitalized_words)

print(capitalize_words("hello world") == "Hello World")  # True
print(capitalize_words("python is fun") == "Python Is Fun")  # True
print(capitalize_words("i love programming") == "I Love Programming")  # True