# Truthiness

# falsy values:
# False
# None
# 0
# 0.0
# 0j
# empty string: ''
# empty list: []
# empty dictionary: {}
# empty tuple: (,)
# empty set: set()
# empty frozenset: frozenset()
# empty range: range()

# an expression returning True or False values
# is different from Python evaluating the
# expression as truthy or falsy

num = 5
if num:
    print("valid number")
else:
    print("error!")

# the above code prints valid number
# Python evaluates any number that is not 0
# to be truthy

print(num == True)      # False

# example of code that uses truthy or falsy
# values
# name = get_name_from_user()
# if name:
#     print(f"Hi {name}")
# else:
#     print("you must enter your name!")


# style guide preferred code style
# name = get_name_from_user()
# if name == "":
#     print("you must enter your name!")
# else:
#     print(f"Hi {name}")