a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def counting(a, b):
    c = round(a / b, 2)
    return c


try:
    counting(a, 0)
except ZeroDivisionError:
    print("You cant divide by zero")

print(counting(a, b))
# выводит ошибку даже если b != 0