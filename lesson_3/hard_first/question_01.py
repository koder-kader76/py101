# Question 1

# Will the following functions return the same results?
# Try to answer without running the code or looking at the solution.

def first():
    return {
        'prop1': 'hi there',
    }

def second():
    return
    {
        'prop1': 'hi there',
    }

print(first())
print(second())


# answer: no
# both functions look similar but the main difference 
# between first() & second() is:
# first returns a dict object - {'prop1': 'hi there'}
# second will return nothing - the dict object is declared
# in the following line which makes it redundant
# so the second() function will execute and when it encounters
# the return keyword will terminate it before it reaches the
# dict object