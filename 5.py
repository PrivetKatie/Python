
def counting():
    numbers = []

    sum_n = 0
    try:
        while True:
            numbers = map(int, input("Введите числа через пробел. Для выхода из программы введите не числовое значение. ").split())

            for i in numbers:
                sum_n += i
            print(sum_n)
    except ValueError:
        print(sum_n)




print(counting())
