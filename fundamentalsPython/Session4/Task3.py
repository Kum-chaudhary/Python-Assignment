# zomato late-night food order

age = int(input("enter a your age :"))
time = int(input("Enter current time(0-23) :"))

if age >=18:
    if time >=22 or time <=2: 
        #22 means 10 PM and 2 means 2 AM.
        print("order allowed ")
    else:
        print("order not allowed")
else:
    print("order not allowed")

"""
output:
enter a your age :18
Enter current time(0-23) :23
order allowed 
"""