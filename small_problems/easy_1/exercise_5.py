# Tip Calculator

# Create a simple tip calculator. The program 
# should prompt for a bill amount and a tip 
# rate. The program must compute the tip, 
# then print both the tip and the total 
# amount of the bill. You can ignore input 
# validation and assume that the user will 
# enter valid numbers.

# Sample 
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

def bill_amount():
    bill = input("What is the bill? ")
    return int(bill)

def tip_percentage():
    tip = input("What is the tip percentage? ")
    return int(tip)

def tip_amount(bill, tip):
    return (bill * tip) / 100

def total_bill(bill, tip):
    return bill + tip

def main():
    bill_pre_tip = bill_amount()
    total_tip = tip_percentage()
    tip = tip_amount(bill_pre_tip, total_tip)
    print(f"The tip is ${tip:.2f}")
    total = total_bill(bill_pre_tip, tip)
    print(f"The total is {total:.2f}")

main()

#LS:
# bill = float(input("What is the bill? "))
# percentage = float(input("What is the tip percentage? "))

# tip = bill * (percentage / 100)
# total = bill + tip

# print(f"The tip is ${tip:.2f}")
# print(f"The total is ${total:.2f}")