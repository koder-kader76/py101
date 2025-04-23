# This assignment covers "look Before You Leap" Concept

def lower_first(word):
    # Ensure word is a string
    if type(word) != str:
        return word
    
    # Ensure word is at least 1 character long
    if len(word) == 0:
        return word
    
    # We now know that word is a string that contains
    # at least one character. That means the following
    # code will run without generating an error.
    return word[0].lower() + word[1:]

print(lower_first("FOO"))   # fOO
print(lower_first(32))      # 32
print(lower_first("JOHN"))  # jOHN 
print(lower_first(""))  # '' 