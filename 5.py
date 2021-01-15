with open('text_5.txt', 'w+', encoding='utf-8') as f:
    from random import randint
    numbers = []
    while len(numbers) < 20:
        n = randint(1, 1000)
        numbers.append(n)
    print(*numbers, sep=', ', file=f)
    print(sum(numbers))
