# Write a function that checks if a string is a 
# palindrome, ignoring spaces, punctuation, and case 
# sensitivity.

def is_palindrome(message):
    if message == '':
        return False

    alpha_chars = [char.lower() for char in message if char.isalpha()]

    cleaned_message = ''.join(alpha_chars)

    return cleaned_message == cleaned_message[::-1]


print(is_palindrome("A man, a plan, a canal: Panama") == True)  # True
print(is_palindrome("race a car") == False)  # True
print(is_palindrome("Was it a car or a cat I saw?") == True)  # True