import re

def is_valid_pnr(pnr):
    pattern = r"^[0-9]{10}$"
    return bool(re.match(pattern, pnr))

pnr = input("Enter 10-digit PNR number: ")

if is_valid_pnr(pnr):
    print("Valid PNR")
else:
    print("Invalid PNR")