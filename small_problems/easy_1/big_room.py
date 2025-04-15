# How big is the room?

# Build a program that asks the user to enter
# the length and width of a room, in meters,
# then prints the room's area in both square
# meters and square feet.

# PEDAC
# get input from user
# input should be numeric value
# 2 inputs - length & width
# calculate area = length * width
# convert area from meters to square feet

# example cases
# 10 * 20 = 200 sq meters & 2147.39 sq ft
# input cannot be 0 or empty
# input can be float or number
# input cannot be large number < 1000

# data structure
# can be an integer or float
# input will be float(str)

# algorithm
# get length from user
#   check if input is valid
# get width from user
#   check if input is valid
# get square_meters = length *  width
# get square_feet = square_meters * 10.7639
# print out room's area in square_meters &
# square_feet

# import math

def invalid_input(input_str):
    try:
        if float(input_str) > 0:
            float(input_str)
        else:
            return True
    except ValueError:
        return True

def get_input(length_str):
    print(f"Please enter {length_str} of room: ")
    input_str = input()

    while invalid_input(input_str):
        print("Please enter a valid number: ")
        input_str = input()

    return input_str

length = float(get_input('length'))
width = float(get_input('width'))

square_meters = round(length * width, 2)
square_feet = round(square_meters * 10.7639, 2)

print(f"Room Area: "
      f"{square_meters} sq meters"
      f" & {square_feet} sq feet.")


# LS:
# length = float(input("Enter the length of the room in meters: "))
# width = float(input("Enter the width of the room in meters: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# print(f"The area of the room is {area_in_meters:.2f} "
#       f"square meters ({area_in_feet:.2f} square feet).")