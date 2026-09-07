# Calculate the customer's due amount

bill_amount = float(input("Enter the bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

due_amount = bill_amount - amount_paid

print("Customer's due amount is:", due_amount)
