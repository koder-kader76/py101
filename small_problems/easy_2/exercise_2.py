# Greeting a user

# Write a program that asks for user's name, 
#   then greets the user. 
# If the user appends a ! to their name, 
#   the computer will yell the greeting 
#   (print it using all uppercase).

# example 1
# What is your name? Sue
# Hello Sue.

# example 2
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

def get_user_name():
    user_name_input = input("What is your name? ")

    while not user_name_input.strip():
        user_name_input = input("Please enter your name? ")
    
    return user_name_input.strip().title()

def greeting():
    user_name = get_user_name()
    
    if user_name.endswith('!'):
        user_name_no_excalamation = user_name[:-1]
        return(f"HELLO {user_name_no_excalamation.upper()}! " 
               "WHY ARE WE YELLING?")
    
    return f"Hello {user_name}."

print(greeting())