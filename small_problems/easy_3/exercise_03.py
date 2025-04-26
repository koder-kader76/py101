# 3. Bannerizer

# Write a function that takes a short line of text and prints it within a box.
import textwrap

def wrap_list(message, width_): 
    return textwrap.wrap(message, width_)

def display_borders(maximum_length):
    border = f"+{(maximum_length * '-')}+"
    return border

def display_spaces(maximum_length):
    spaces = f"|{(maximum_length * ' ')}|"
    return spaces

def display_message(words_list, width):
    if words_list != []:
        for words in words_list:
            print(f"| {words.center(width)} |")
    else:
        print(f"|{(width + 2) * ' '}|")

def print_in_box(text, max_width=1):

    phrase_list = wrap_list(text, max_width)

    borders = display_borders(max_width + 2)
    spaces = display_spaces(max_width + 2)

    print(borders)
    print(spaces)
    
    display_message(phrase_list, max_width)

    print(spaces)
    print(borders)


print_in_box('To boldly go where no one has gone before.', 30)
print_in_box('')
line = """Your solution correctly addresses the requirements of the exercise, creating a box around the provided text with appropriate borders and spacing. You've taken a clean approach that handles both the provided examples effectively, including the empty string case."""
print_in_box(line, 42)