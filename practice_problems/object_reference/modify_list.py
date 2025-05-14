def modify_list(lst):
    lst.append(4)
    print(lst)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)

# Identify the output of this code:
# The last 2 lines, the modify_list(numbers) and print(numbers) will output [1, 2, 3, 4]. numbers is assigned to a list object which is passed into the modify_list function. In the function, the lst.append method mutates the caller and changes the original object which numbers is referencing.
# This code demonstrates that the an object is passed by reference as an argument and depending on the object's mutability and the operation performed within the function, the object may be mutated or re-assigned.