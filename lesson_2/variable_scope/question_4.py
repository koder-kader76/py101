# Question 4

# What will the following code print and why? 
# Don't run it until you have tried to answer.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# output: 'Hello World'
# when the outer() function is invoked, 
# it will invoke the inner() function
# during the print call, Python will get inner_var
# from the function itself but since the outer_var
# is not defined in the inner(), it will look for 
# variable in a lexical scope, meaning it will look
# for the variable in the nearest outer scope
# and take the value from the outer()