# flipcart product description - first word , last word, and total

description = input("enter product description:")

words = description.split()

if len(words) > 0:
    print("First word :",words[0])
    print("last word :",words[-1])
    print("total word :",len(words))
else:
    print("No word entered")