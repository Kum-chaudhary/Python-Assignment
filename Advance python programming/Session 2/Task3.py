# create order.txt 

with open("orders.txt", "r") as file:
    while True:
        line = file.readline()

        if not line:
            break

        print("Order:", line.strip())
        print("File pointer position:", file.tell())        