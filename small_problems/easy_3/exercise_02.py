# 2 ddaaiillyy ddoouubbllee

# Write a function that takes a string argument and returns a new 
# string that contains the value of the original string with all 
# consecutive duplicate characters collapsed into a single 
# character.

import re

# my original solution
def crunch(message):
    crunched = ''
    
    for char in message:
        if not crunched.endswith(char):
            crunched += char

    return crunched

# Further exploration using re module
# solution taken from stack overflow for import re
def crunch2(message):
    return re.sub(r'([a-z0-9])\1+', r'\1', message)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')