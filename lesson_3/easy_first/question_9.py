# Question 9

# Print a new version of the sentence given by advice that ends 
# just before the word house. Don't worry about spaces or 
# punctuation: remove everything starting from the beginning of 
# house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

short_advice = advice[:advice.find('house')].strip()
print(repr(short_advice))

# LS:
# print(advice.split('house')[0])