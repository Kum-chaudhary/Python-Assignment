# reverse message without reverse() or [::-1]

def reverse_message(message):
    reverse = ""

    for char in message:
        reverse = char + message
    return reverse

text = input("Enter your message :")
print("Reverse message :",reverse_message(text))
    


