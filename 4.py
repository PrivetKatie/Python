class Car:

    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.i_p = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn_direction(self):
        print('Turn direction')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Превышение скорости!")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


auto_1 = WorkCar(65, 'Red', 'Ford', 'yes')

auto_1.show_speed()