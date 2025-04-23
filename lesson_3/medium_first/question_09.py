# Question 9

# Consider these two simple functions:
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?
print(bar(foo())) # --> bar(foo())

# The function will return False
# the bar function is taking in foo() as an argument
# foo() will evaluate to 'yes' which gets passed in an argument
# (param == "no") will evaluate to False 
# since the operation is an 'and' operation
# it will short-circuit the expression and return