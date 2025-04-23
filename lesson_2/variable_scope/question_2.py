# Question 2

# What will the following code print and why? Don't run it until 
# you have tried to answer.

num = 5

def my_func():
    num = 10

my_func()
print(num)

# output: 5
# print(num) will access the global variable num 
# which references 5
# the num assigned within the function is a local
# variable and cannot be accessed from outside
# the function