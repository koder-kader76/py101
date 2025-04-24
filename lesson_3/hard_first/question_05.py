# Question 5

# What do you expect to happen when the greeting variable is 
# referenced in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

# NameError: name 'greeting' is not defined
# the greeting variable is inside an if block
# which never executes as the expression evaluates 
# to False - so the greeting variable is never initialized
