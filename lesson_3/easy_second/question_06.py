# Question 6

# Back in the stone age (before CSS), we used spaces to align 
# things on the screen. If we have a 40-character wide table of 
# Flintstone family members, how can we center the following 
# title above the table with spaces?

title = "Flintstone Family Members"
print(repr(title.center(40, '')))
# '       Flintstone Family Members        '

print(repr(title.center(40, 'x')))
# 'xxxxxxxFlintstone Family Membersxxxxxxxx'