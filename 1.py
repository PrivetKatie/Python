with open('text.txt', 'a+', encoding='utf-8') as f:
    while True:
        text = input("Введите текст, чтобы добавить его в файл. Чтобы прекратить - оставьте строку пустой. ")
        print(text, file=f)
        if text == '':
            break