earn = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
if earn > costs:
    print("Поздравляем, вы в плюсе!")
    profit = int(earn - costs)
    rent = int((profit / earn) * 100)
    if profit > 0:
        print("Рентабельность - " + str(rent) + "%")
    people = int(input("Cколько человек работают у вас в компании? "))
    people_profit = int(profit / people)
    print("На одного работника прибыль составила: " + str(people_profit))
elif earn < costs:
    print("К сожалению вы работаете в убыток :(")
else:
    print("Идете ровно!")
