# stop "burger king" using break

foods = ['burger','pizza','sandwhich','pasta','burger king']
for food in foods:
    if food == 'burger king':
        print("Found burger king, stop search")
        break
    print(food)
