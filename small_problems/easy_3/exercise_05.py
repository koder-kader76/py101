# 5 Right Triangles

# Write a function that takes a positive integer, n, as an 
# argument and prints a right triangle whose sides each have n 
# stars. The hypotenuse of the triangle (the diagonal side in the 
# images below) should have one end at the lower-left of the 
# triangle, and the other end at the upper-right.

def triangle(height):
    for row_num in range(1, height + 1):
        stars = '*' * row_num
        print(stars.rjust(height))

triangle(5)
triangle(9)