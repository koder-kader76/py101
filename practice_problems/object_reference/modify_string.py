def modify_string(s):
    s = s + " World"
    print(s)

greeting = "Hello"
modify_string(greeting)
print(greeting)

# What will the following code output and why?
# In line 6, during the function call, the code will output "Hello World". The function itself performs a string concatenation with " World". 
# In the last print call, the output will be "Hello". The greeting variable is defined in the global scope and is not affected by the string operation in the function.
# This code demonstrates how arguments passed into functions are references to objects. Any assignment within the function will make the variable a local variable and within the function scope which means it cannot be accessed outside of the function.