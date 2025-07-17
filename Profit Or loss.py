CP = float(input("Enter your Cost-Price = "))
SP = float(input("Enter your Selling-Price = "))
if (SP>CP):
    amount = SP - CP
    print("Total Profit", amount)
else:
    print("No Profit")    