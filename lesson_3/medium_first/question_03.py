# Question 3

# Alyssa was asked to write an implementation of a rolling 
# buffer. You can add and remove elements from a rolling buffer. 
# However, once the buffer becomes full, any new elements will 
# displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements 
# to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# What is the key difference between these implementations?

# add_to_rolling_buffer1: In this implementation, the new_element is added to the buffer using the append method which performs mutation of the list object

# add_to_rolling_buffer2: In this implementation, the buffer element is concatenated with the new_element list - in this instance, it performs re-assignment of the buffer object to reference a new list object

# LS:
# Yes, there is a difference. The first function 
# (add_to_rolling_buffer1) mutates the original list represented 
# by buffer. The second function (add_to_rolling_buffer2) does 
# not mutate the original list, but instead creates a new list 
# and assigns it to buffer, whose value ultimately gets returned 
# by the function.