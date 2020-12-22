number = int(input("Введите число!"))
max_number = 0
while number > 0:
    x = number % 10
    if x >= max_number:
        max_number = x
    number = number // 10
print(max_number)


