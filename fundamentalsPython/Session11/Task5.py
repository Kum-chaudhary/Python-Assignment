def update_cart(cart, item, qty):
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    return cart


cart = {
    "Laptop": 1,
    "Mouse": 2
}

cart = update_cart(cart, "Keyboard", 1)
cart = update_cart(cart, "Mouse", 3)

print(cart)