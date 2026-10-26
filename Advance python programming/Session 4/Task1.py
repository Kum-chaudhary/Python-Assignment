class invalidCouponCodeError(Exception):
    pass

valid_coupon = ["Save10","Food20","Welcome"]

def apply_coupon(coupon_code):
    if coupon_code not in valid_coupon:
        raise invalidCouponCodeError("Invalid coupon Error !")
    else:
        print("coupon applied sucessfully !")


try:
    coupon = input("Enter Coupon code:")
    apply_coupon(coupon)
except invalidCouponCodeError as e:
    print(e)

