# Question 1

# What will the following code print and why? Don't run it until 
# you have tried to answer.

num = 5

def my_func():
    print(num)

my_func()

# output: 5
# In this code, the num variable is being used without assignment
# so when my_func() is invoked, Python will look for the num
# variable in the outer scope and print the value 5