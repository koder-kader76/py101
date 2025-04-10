# example of Python uses True and False values
# print them
# assign them to variables
# pass them around
# test them

print(True)     # True
print(False)    # False

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string


print(make_longer("abc", True))     # abcabc
print(make_longer("xyz", False))    # xyz


def is_digit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False
    
print(is_digit("5"))       # True 
print(is_digit("a"))       # False


value = True
if value is True:
    print("It's true!")
elif value is False:
    print("It's false!")
else:
    print("It's not true or false!")

# It's true!