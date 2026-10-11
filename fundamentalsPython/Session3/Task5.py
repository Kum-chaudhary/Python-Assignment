# basic calculator 

num1 = float(input("enter a first number:"))
operator = input("Enter operator(+,-,*,/) :")
num2 = float(input("enter a second number:"))

if operator == "+":
    result = num1 + num2
    print("Result :",result)

elif operator == "-":
    result = num1 - num2
    print("Result :",result) 

elif operator == "*":
    result = num1 * num2
    print("Result :",result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result :",result)
    else:
        print("Error : it's not divided by 0")

else:
    print("Error : Invalid operator")


"""
output :
enter a first number:44
Enter operator(+,-,*,/) :+
enter a second number:78
Result : 122.0
"""

