# 10. When Will I Retire?

# Build a program that displays when the user will retire and how 
# many years she has to work till retirement.

# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

from datetime import date

def prompt(message):
    print(f"==> {message}", end='')

def is_invalid_age(input_age):
    return not input_age.isdigit()

def get_age(message_):
    prompt(message_)
    age = input()

    while is_invalid_age(age):
        prompt("Please enter a valid age. ")
        age = input()
    
    return int(age)

def difference_in_years(current, retirement):
    difference = retirement - current
    return difference

def this_year():
    return date.today().year

def display_retirement(year, difference_years):
    prompt(f"It's {year}. " 
           f"You will retire in {year + difference_years}\n")
    prompt(f"You have only {difference_years} years of work to go!\n")

def main():
    current_age = get_age("What is your age? ")

    retirement_age = get_age("At what age would you like to retire? ")

    difference = difference_in_years(current_age, retirement_age)

    current_year = this_year()

    display_retirement(current_year, difference)

main()