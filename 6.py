with open('text_6.txt', 'r', encoding='utf-8') as f:
    sub = []
    hours = []
    d = {}

    import re

    for line in f:
        key, value = line.split(':')
        sub.append(key)
        n = re.findall(r'\d+', value)
        hour = sum(map(int, n))
        hours.append(hour)

    d = dict(zip(sub, hours))
    print(d)




