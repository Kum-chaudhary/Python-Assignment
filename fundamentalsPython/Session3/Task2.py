#sum, difference,product, and quotient

num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))

print("sum :",num1 + num2)
print("Difference :",num1 - num2)
print("Product:",num1 * num2)

if num2 != 0:
    print("Quotient:",num1 / num2)
else:
    print("can not divided by 0.")

"""
output:
Enter a first number:12
Enter a second number:2
sum : 14
Difference : 10
Product: 24
Quotient: 6.0
"""    