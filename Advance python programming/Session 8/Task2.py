import math

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

bmi = weight / math.pow(height,2)
print("Youe bmi is :",round(bmi,2))