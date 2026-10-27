orders = {}

def add_order(order_id,restaurant,items,total):
    orders.setdefault(order_id,{})
    orders[order_id]["restaurant"] = restaurant
    orders[order_id]["items"] = items
    orders[order_id]["Total"] = total

    print("order added sucessfully !")

def update_total(order_id,new_total):
    if order_id in orders:
        orders[order_id]["Total"] = new_total
        print("total update sucessfully !")
    else:
        print("order not found !")

add_order(101,"Pizza hut",["Pizza","coke"],450)
add_order(102,"Dominos",["Burger","Fries"],300)

update_total(101,500)
print(orders)
