# Question 6

# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)   # 34

# The output will be 34.
# the answer is referencing 42 throughout the program
# when answer is passed into the function, the variable becomes a local variable and is not accessible outside of the function
# the return value is now referenced by new_answer