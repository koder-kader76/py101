# Question 6

# Determine whether the name Dino appears in the strings below -- 
# check each string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def find_text(sentence, text):
    return text in sentence

print(find_text(str1, 'Dino'))
print(find_text(str2, 'Dino'))