with open('text_7.txt', 'r', encoding='utf-8') as f:
    names = []
    profits = []
    d = {}
    d_profit = {}
    for line in f:
        name, form, all_money, costs = line.split()
        profit = int(all_money) - int(costs)
        names.append(name)
        profits.append(profit)
    sum_profit = 0
    for el in profits:
        if el > 0:
            sum_profit += profit
    average_profit = sum_profit / 5
    d_profit = {"average profit": average_profit}

    d = dict(zip(names, profits))


    print(d)
    print(d_profit)