try:
    price = float(input("Enter Your price:"))
    quantity = int(input("Enter your Quantity:"))

    total = price * quantity

    print("Total amount order :",total)

except ValueError:
    print("Error : Please enter valid value!")    