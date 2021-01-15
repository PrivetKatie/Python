d = {}
with open('text_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key, value = line.split()
        d[key] = float(value)
    print(d)
    print(sum(d.values()))

    for key, value in d.items():
        value = float(value)
        if value < 20000:
            print(key)





