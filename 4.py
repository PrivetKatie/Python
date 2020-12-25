user_list = input("Напишите произвольное количество слов через пробел: ")

user_list = user_list.split()
for i, item in enumerate(user_list, 1):
    print(i, item[:10])



