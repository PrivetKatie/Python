class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return round(self.quantity / other.quantity)

    def make_order(self, number):
        cells_in_order = ''
        for i in range(int(self.quantity / number)):
            cells_in_order += f'{"*" * number} \n'
        return cells_in_order


cell_1 = Cell(55)
cell_2 = Cell(10)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))