# Question 5

# The following function unnecessarily uses 
# two return statements to return boolean 
# values. Can you rewrite this function so it 
# only has one return statement and does not 
# explicitly use either True or False?

# Try to come up with two different solutions.
COLORS = {'blue', 'green'}

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def is_color_valid1(color):
    return color in COLORS

def is_color_valid2(color):
    return color in ('blue', 'green')

def is_color_valid3(color):
    bg_colors = {
        'colors': ['blue', 'green'],
    }

    return color in bg_colors['colors']

def is_color_valid4(color):
    return (
        color == "blue" or color ==  "green"
    )

print(is_color_valid4('black'))