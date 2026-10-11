#Infinite Loading Spinner with break

count = 0
while True:
    print("Loading...")
    count += 1

    if count == 3:
        break

"""
output:

Loading...
Loading...
Loading...
"""    