bill = float(input("Enter your total bill amount : ₹"))
paid = float(input("Enter the amount you have paid : ₹"))

def calculate_due( bill_amount , amount_paid ) :
    due_amount = bill_amount - amount_paid
    if due_amount < 0 :
        print("Customer has Overpaid, Extra amount to return : ₹" , abs(due_amount))
    elif due_amount == 0 :
        print("Customer has fully paid the bill. No due amount. ")
    else:
        print("Customer still owes : ₹" , due_amount)

calculate_due( bill , paid)