# Profit loss
actual_cost = float(input("Please enter the actual cost of the item: "))
sale_amount = float(input("Please enter the sale amount of the item: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("The profit is: ", amount)

else:
    print("No profit!!!")