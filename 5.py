class Stationery:

    title = 'Title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркером')


pen_1 = Pen()
pen_1.draw()