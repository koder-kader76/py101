# EAFP: It's Easier to Ask Forgiveness than Permission

def lower_first(word):
    try:
        return word[0].lower() + word[1:]
    except (TypeError, IndexError):
        return word
# Handle exceptions by returning `word` as-is

print(lower_first("FOO"))  
# Output: "fOO"
print(lower_first(32))     
# Output: "32"
print(lower_first(''))     
print(lower_first('123abc'))     

# EAFP approach:
# try code block
#   run if execution successful
#   handle if exceptions 

# preferred for it concise structure