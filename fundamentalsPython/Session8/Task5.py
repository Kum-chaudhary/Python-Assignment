# mask a phone number - paytm style

def mask_phone_number(phone):
    return "*" * 6 + phone[-4]

phone = int(input("Enter 10 digit phone number:"))

if phone.isdigit() and len(phone) == 10:
    print("Mask Phone Number :",mask_phone_number(phone))
else:
    print("Please enter 10 digit number")