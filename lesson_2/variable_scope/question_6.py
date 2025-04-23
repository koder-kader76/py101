# Question 6

# What will the following code print and why? 
# Don't run it until you have tried to answer.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# output: Inner 1: 25
# output: Inner 2: 15
# inner_func1() x is already within the function
# Python will use its value to print 
# inner_func2() x is not defined within the function
# Python will look for nearest scope for the x variable
# retrieve the value defined in my_func()