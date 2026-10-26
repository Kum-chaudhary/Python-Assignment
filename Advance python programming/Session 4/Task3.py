class paymentFailedError(Exception):
    pass
def process_payment(amount):
    if amount <= 0:
        raise paymentFailedError("Invalid payment amount !")

    else:
        print("Payment sucessfully")

try:
    process_payment(500)
except paymentFailedError as e:
    print(e)        