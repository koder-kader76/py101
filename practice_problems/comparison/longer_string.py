def first_is_longer(str1, str2):
    if not str1:
        return False
    
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False

    return len(str1) > len(str2)
        
# Test cases
print(first_is_longer("hello", "hi"))  # True
print(first_is_longer("hi", "hello"))  # False
    