# use both continue and break

messages = ['Hi','spam','Hello','spam','How are you?']

for message in messages:
    if message == 'spam':
        continue
    if message == 'How are you?':
        break
    print(message)