# Types of Errors

# NameError - when a variable hos not been defined
# a     # referencing an undefined variable
# a()   # when calling an undefined function

# TypeError - when a value of the wrong type is being used in an expression

# using an argument of the wrong type as function argument
# my_str = "abc"
# my_str.find(42)
# TypeError: must be str, not int

# trying to call an object which isn't callable
# my_int = 42
# my_int()


# SyntaxError - when Python sees code that violates its sytactic rules

# print('hello)
# SyntaxError: unterminated string literal (detected at line 1)

# SyntaxErrors are caught during the parsing phase - when it is loading the program - the errors are raised based on the code itself and not during execution

# def (
# SyntaxError: invalid syntax

# in some cases, SyntaxError is raised during code execution
# expression = "2 * (3 + 4)"
# result = eval(expression)

# code uses Python's eval function which basically reads like this
# result 2 * (3 + 4

# key difference
# SyntaxError with eval is while the code is being executed
# SyntaxError for the result is when the code is being parsed (before execution)

# ValueError - occurs during function call when argument is correct type but the object value is inappropriate
# e.g
# number = int('abc')


# IndexError - raised when trying to access an index from outside of the range of indexes
# e.g
# number = [1, 2]
# print(number[2])
# IndexError: list index out of range


# KeyError - raised when a key in a dictionary doesn't exist
# e.g
# my_dict = {'a': 1, 'b': 2}
# my_dict['c']
# KeyError: 'c'


# ZeroDivisionError
# 2 occasions when it occurs

# 1. when trying to divide an integer by 0
# 1100 / 0
# ZeroDivisionError: division by zero

# 2. when 0 on the right side of %
# 100 % 0
# ZeroDivisionError: integer modulo by zero


