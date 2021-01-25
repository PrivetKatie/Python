class Clothes:
    pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def count_cloth(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def count_cloth(self):
        return 2 * self.h + 0.3


my_suit_1 = Suit(150)
my_coat_1 = Coat(44)
print(round(my_suit_1.count_cloth + my_coat_1.count_cloth))