def my_func(a, b, c):
    numbers = [a, b, c]
   # a = int(input("Введите первое число: "))
   # b = int(input("Введите второе число: "))
   # c = int(input("Введите третье число: "))
    numbers.sort()
    return numbers[-2], numbers[-1]


print(my_func(77,5,44))