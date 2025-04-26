# 1. Repeat Yourself

# Write a function that takes two arguments, a string and a 
# positive integer, then prints the string as many times as the 
# integer indicates.

def repeat(text, multiple):
    for _ in range(multiple):
        print(text)

repeat('Hello', 3)
repeat('Goodbye', 5)