my_list = [7, 5, 3, 3, 2]
number = int(input("Введите целое число! "))
for i in range(len(my_list)):
    if my_list[i] == number:
        my_list.insert(i + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
    elif my_list[-1] > number:
        my_list.append(number)
    elif my_list[i] > number and my_list[i + 1] < number:
        my_list.insert(i + 1, number)
        break
print(my_list)