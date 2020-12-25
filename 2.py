user_list = input("Введите произвольное количество элементов через запятую: ")

user_list = user_list.split(",")
el = 0
for elem in range(int(len(user_list)/2)):
    user_list[el], user_list[el + 1] = user_list[el + 1], user_list[el]
    el +=2

print(user_list)