food_order = {
    "pizza": 2,
    "burger":1,
    "fries":3
}
print(food_order)
# Print all food items
print("Food Items:", food_order.keys())

# Print all quantities
print("Quantities:", food_order.values())

# Print each item with its quantity
print("Items with Quantity:")
for item, qty in food_order.items():
    print(item, ":", qty)