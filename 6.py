start = int(input("Введите, сколько км вы можете пробежать: "))
result = int(input("Введите цель: "))
day = 1
day_progress = float(start * 0.1)
while start < result:
    print("День " + str(day) + ": " + str(round(start, 3)))
    start = float(start + day_progress)
    day = day + 1
print("На " + str(day) + " вы достигнете результата в " + str(result) + " км.")