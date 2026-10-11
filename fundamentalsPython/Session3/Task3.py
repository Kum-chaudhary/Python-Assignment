# zomato type bill calculator 

price = float(input("Enter a food item price:"))
quantity = int(input("Enter quantity:"))

total = price * quantity #calculates total.

print(f"your total bill is a {total:.2f}.") # .2f exactly 2 decimal places

"""
output:
Enter a food item price:12.4
Enter quantity:2
your total bill is a 24.80.
"""