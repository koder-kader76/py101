# Question 2

# Alan wrote the following function, which was intended to return 
# all of the factors of number:

def factors(number):
    divisor = number
    result = []

    # change this line from divisor != 0
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    
    return result

# Alyssa noticed that this code would fail when the input is a 
# negative number, and asked Alan to change the loop. How can he 
# make this work? Note that we're not looking to find the factors 
# for negative numbers, but we want to handle it gracefully 
# instead of going into an infinite loop.

# Bonus Question: What is the purpose of number % divisor == 0 in that code?
# the function returns a factors of all numbers, meaning all the numbers that are divisible by the number 
# this operations filters the numbers that are divisible by number and if it is, performs an integer division and adds it to the result

print(factors(10))