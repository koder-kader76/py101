def modify_nested(data):
    data["numbers"].append(4)
    data = {"numbers": [10, 20, 30]}
    print(data)

my_data = {"numbers": [1, 2, 3]}
modify_nested(my_data)
print(my_data)

# Intermediate​: What will this code output and why?

# my_data is initialized with a dictionary object {"numbers": [1, 2, 3]}. During modify_nested(my_data) function call, my_data is passed into the function. data["numbers"].append(4) in the function will add 4 to the end of the list of my_data as they are both referencing the same object. my_data is now referencing {"numbers": [1, 2, 3, 4]}. 
# When data is assigned to {"numbers": [10, 20, 30]}, the my_data becomes a local variable and does not affect the original my_data reference in the global scope. During the print call in the function, the output will be {"numbers": [10, 20, 30]}
# In the last print call, my_data will output {"numbers": [1, 2, 3, 4]} showing that the original object has been mutated. 
# This code shows how arguments passed into functions are references to objects and based on the operation performed in the function, references to objects will either be changed or the object themselves will be changed.