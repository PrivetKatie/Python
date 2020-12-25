goods = []
dictionary = {'name': [], 'price': [], 'amount': [], 'num': []}
good = []
amount = int(input("Введите кол-во товара: "))
n = 1
while n <= amount:
    good = dict({'name': input("Введите название товара: "), 'price': input("Укажите цену: "),
                 'amount': input("Введите количество: "), 'num': input("Укажите едницы измерения: ")})
    goods.append((n, good))
    dictionary = dict(
        {'name': good.get('name'), 'price': good.get('price'), 'amount': good.get('amount'), 'num': good.get('num')})
    n += 1

while True:
    menu = input("Ввести данные о товаре - введите 'Data'\nПосмотреть аналитику - 'Analyse'\n Выйти - 'Exit'").lower()
    if menu == "exit":
        break
    elif menu == "data":
        print(goods)
    elif menu == "analyse":
        print(dictionary)

# Почему-то добавляется в словарь только последний товар, не получается исправить