def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        discount = amount * 0.10
        final_amount = amount - discount
        print("Discount:", discount)
        print("Final Amount:", final_amount)
    else:
        print("No discount applied.")
        print("Final Amount:", amount)


# Without coupon code
apply_coupon(1000)

# With valid coupon code
apply_coupon(1000, "SAVE10")