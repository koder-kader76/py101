# Multiples of 3 and 5

# Write a function that computes the sum of all numbers between 1
# and some other number, inclusive, that are multiples of 3 or 5.
# For instance, if the supplied number is 20, the result should
# be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

def multisum(number, factors=(3,5)):

    multiples = set()

    for factor in factors:
        initial = factor
        while initial <= number:
            multiples.add(initial)
            initial += factor

    return sum(multiples)

print(multisum(1000, (3,4,5,6,7,8)))