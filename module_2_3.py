my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = 0
n = len(my_list)
while 1 > 0:
    my_number = my_list[k]
    if my_number > 0:
        print(my_number)
        k = k + 1
        continue
    elif my_number == 0:
        k = k + 1
        continue
    else:
        break
