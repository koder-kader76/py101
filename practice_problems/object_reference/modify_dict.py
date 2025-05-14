def modify_dict(d):
    d["name"] = "Alex"
    d = {"name": "Taylor", "age": 30}
    print(d)

person = {"name": "Jordan", "age": 25}
modify_dict(person)
print(person)

# Intermediate: Predict the output of the following code
# In line 7, when modify_dict(person) is called, it will output {"name": "Taylor", "age": 30}. d["name"] = "Alex" re-assigns an value within a dictionary which mutates the original object. Following that, the person reference is assigned to another dictionary which makes it a local variable and it is now referencing an entirely new dictionary object.
# In the last print call on person, it will output {"name": "Alex", "age": 25} which was modifed in the first line of the function and changes the original object which person is referencing. With the re-assignment, the person reference becomes a local variable and does not affect the object which the global person is referencing.
# This code demonstrates the difference between re-assignment and mutation when arguments are passed by reference to objects and depending on the operation performed inside the function, the reference to the object will be changed or the object itself will be mutated without changing the reference.