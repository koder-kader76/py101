# Question 1

# Write two different ways to remove all of 
# the elements from the following list:

numbers = [1, 2, 3, 4]

# first method: using pop(0)
while len(numbers):
    numbers.pop(0)

print(numbers)


numbers = [1, 2, 3, 4]

# 2nd method: using list.clear()
numbers.clear()
print(numbers)

# LS:
# while numbers:
#    numbers.pop()