# Question 8

# In the previous problem, our first answer added 'Dino' to the list like this:

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")

# How can we add multiple items to our list (e.g., 'Dino' and 
# 'Hoppy')? Replace the call to append with another method 
# invocation.

# first method: using extend
flintstones.extend(('Dino', 'Hoppy', 'Yabba_Dabba_Doo'))

# second method: using concatenation
flintstones += ('Dino', 'Hoppy', 'Yabba_Dabba_Doo')
print(flintstones)
