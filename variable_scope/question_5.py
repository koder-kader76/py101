# Question 5

# What will the following code do? 
# Don't run it until you have tried to answer.

def my_func():
    num = 10

my_func()
print(num)

# output: NameError: name 'num' is not defined
# num variable is a local variable 
# it cannot be accessed from outside the function
# so an error will be raised