# Question 4

# Using the following string, print a string that contains the 
# same value, but using all lowercase letters except for the 
# first character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

def titlize(phrase):
    words = phrase.translate(str.maketrans({'.': ''})).split()
    capitalize_words = []

    for word in words:
        match word:
            case '.':
                capitalize_words.append('')
            case 'and':
                capitalize_words.append("&")
            case _:
                capitalized_word = word[0].upper() + word[1:].lower()
                capitalize_words.append(capitalized_word)
    
    return ' '.join(capitalize_words)

print(titlize(munsters_description))
# The Munsters Are Creepy & Spooky

print(munsters_description.title())
#The Munsters Are Creepy And Spooky.

print(munsters_description.capitalize())
# The munsters are creepy and spooky.