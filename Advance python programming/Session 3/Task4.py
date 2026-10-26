my_list = [1,2,3]
my_dict = {'a':1}

try:
    print(my_list[5])

except IndexError:
    print("Error : list index out of range")

try:
    print(my_dict['b'])

except KeyError:
    print("Error : dictionary key in not fount !")
