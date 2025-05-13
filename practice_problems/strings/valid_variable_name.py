# Implement a function that validates if a given string is 
# a valid Python variable name. A valid variable name 
# starts with a letter or underscore, followed by any 
# number of letters, numbers, or underscores.

def is_valid_variable_name(string):
    if not string:
        return False
    
    if not (string[0].isalpha() or string[0] == '_'):
        return False
    
    for char in string[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    
    return True


print(is_valid_variable_name("variable_name") == True)  # True
print(is_valid_variable_name("123variable") == False)  # True
print(is_valid_variable_name("_private") == True)  # True
print(is_valid_variable_name("my-var") == False)  # True