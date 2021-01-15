d = ['Один', 'Два', 'Три', 'Четыре']

with open('text_new3.txt', 'x', encoding='utf-8') as f_2:
    with open('text_4.txt', 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            name, number = line.split('-')
            name = d[i]
            i += 1
            print(name, number, file=f_2)