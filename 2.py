class Road:

    _length = None
    _width = None
    weight = None
    number_sm = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('')

    def mass_count(self):
        self.weight = 25
        self.number_sm = 0.5
        a_mass = self.length * self.width * self.weight * self.number_sm
        print(f'Необходимо {a_mass} тонн')


road_1 = Road(20, 5000)
road_1.mass_count()