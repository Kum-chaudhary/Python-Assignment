import re

text = "Contact us at 9876543210 or 9123456789 for help."

pattern = r"\b[0-9]{10}\b"

result = re.search(pattern, text)

if result:
    print("Mobile Number:", result.group())
else:
    print("Mobile number not found")