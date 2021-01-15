with open('text_3.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    size = len(content)
    print(size)
with open('text_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(len(line.split()))

