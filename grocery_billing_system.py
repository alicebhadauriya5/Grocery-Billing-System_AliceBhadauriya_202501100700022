# Grocery Store Billing System
# Case Study 1
# Subject: Python for Engineers (AI102P)

# Taking input prices for 3 items
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Calculating total cost
total = item1 + item2 + item3

# Initial discount
discount = 0

# Applying 10% discount if total exceeds $50
if total > 50:
    discount = total * 0.10

# Final payable amount
final_amount = total - discount

# Displaying the results
print("\n----- BILL DETAILS -----")
print(f"Original Total: ${total:.2f}")

if discount > 0:
    print(f"Discount Applied: ${discount:.2f}")
else:
    print("Discount Applied: $0.00")

print(f"Final Payable Amount: ${final_amount:.2f}")