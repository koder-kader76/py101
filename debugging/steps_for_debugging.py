# steps for debuggin
# 1. reproduce the error
# programmers need to find a way to reproduce 
# the error - only then they can isolate the 
# problem

# 2. determine boundaries of error
#   once you can consistently reporduce the 
# problem - tweak the data that caused the 
# error

# stack trace error caused by this code
# return list(filter(lambda x: x % 2 == 0, 
# numbers))

# 3. trace the code
# once you understand the boundaries of 
# the problem, you can start to trace the 
# code     

# e.g
def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    print(grades)
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'},
    {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

# 1. reproduce the problem
# students = [
#     {'name': 'Alice', 'grade': 85},
# ]
# 85.0

# students = [
#      {'name': 'Bob'},
# ]
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

# students = [
#     {'name': 'Alice', 'grade': 100},
#     {'name': 'Bob', 'grade': 0},
# ]
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        if grade != None:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))

# TypeError: unsupported operand type(s) for 
# +: 'int' and 'NoneType'