# Question 3

# Programmatically determine whether 42 lies between 10 and 100, 
# inclusive. Do the same for the values 100 and 101.

def is_inbetween(number, start, end):
    numbers_range = range(start, end + 1)

    return number in numbers_range

print(is_inbetween(42, 10, 100))
print(is_inbetween(100, 10, 100))
print(is_inbetween(101, 10, 100))