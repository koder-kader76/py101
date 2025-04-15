# Exception Handling

try:
    num_str = input("Enter a number: ")
    num = int(num_str)

    result = 10 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Exception handling complete")

# ValueError - if user enters a non-integer value, program displays error

# ZeroDivisionError - if user enters '0' value, program warns about value

# else - when no errors are detected, the result is printed

# finally - when the execution is completed, the final message is displayed