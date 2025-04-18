# Assignment: Mortgage / Car Loan Calculator

# build a mortgage calculator

# You'll need three pieces of information:
#   the loan amount
#   the Annual Percentage Rate (APR)
#   the loan duration

# From the above, you'll need to calculate the following two
# things:
#       monthly interest rate (APR / 12)
#       loan duration in months

# m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

# When you write your program, don't use the single-letter
# variables m, p, j, and n; use explicit names. For instance, you
# may want to use loan_amount instead of p.

# Try to print the payment amount as a dollar and cents amount, e.
# g., $123.45 or $371.00.

# PEDAC
# get input from user
    # loan amount
    # annual percentage rate
    # loan duration
# calculate monthly interest rate
# loan duration in months
# calculate loan in months

import math

def prompt(message):
    print(f"==> {message}")

def isvalid_loan(amount_str):
    try:
        amount = float(amount_str)
        return amount >= 1000
    except ValueError:
        return False

def get_loan_amount():
    prompt("Please enter loan amount: ")

    while True:
        loan_request = input()

        if isvalid_loan(loan_request):
            return float(loan_request)
        prompt("Please enter a valid amount: ")

def isvalid_interest(interest_str):
    try:
        interest = float(interest_str)
        return interest > 0
    except ValueError:
        return False

def get_interest_rate():
    prompt("Please enter interest rate: ")

    while True:
        interest = input()

        if isvalid_interest(interest):
            return float(interest) / 100
        prompt("Please enter a valid number. ")

def isvalid_duration(duration_str):
    try:
        duration = float(duration_str)
        return duration > 0
    except ValueError:
        return False

def get_duration():
    prompt("Please enter loan duration (in years): ")

    while True:
        duration = input()

        if isvalid_duration(duration):
            total_duration = math.ceil(float(duration) * 12)
            return total_duration
        prompt("Please enter a valid number. ")

def interest_rate(interest):
    return interest / 12

def mortgage_calculator():
    loan_amount = get_loan_amount()
    annual_rate = get_interest_rate()
    loan_duration = get_duration()
    monthly_interest = interest_rate(annual_rate)

    monthly_payment =    (loan_amount
                      *  (monthly_interest
                      /  (1 - (1 + monthly_interest)
                      ** (-loan_duration))))

    prompt(f"Loan Amount: ${loan_amount:,.2f}")
    prompt(f"Annual Interest Rate: {annual_rate * 100:.2f}%")
    prompt(f"Loan Duration: {loan_duration // 12} years,"
           f"{loan_duration % 12} months)")
    prompt(f"Your monthly payment is: ${monthly_payment:,.2f}")

    return f"${monthly_payment:,.2f}"

def main():
    while True:
        prompt("Welcome to Mortgage Calculator")
        prompt("------------------------------")
        prompt(f"Monthly payment: {mortgage_calculator()}")

        prompt("Would you like to perform another calculation?")
        answer = input().lower()

        if answer not in ['y', 'yes']:
            prompt("Thank you for using Mortgage Calculator!")
            break

main()
