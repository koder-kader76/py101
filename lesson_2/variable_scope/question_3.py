# Question 3

# What will the following code print and why? 
# Don't run it until you have tried to answer.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# output: 10
# in this code, the global keyword is used
# so python will reference num from the outer scope
# and changes what the num variable references
# when the function is invoked