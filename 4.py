class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn_direction(self):
        print('Turn direction')

    def show_speed(self):
        print(self.speed)


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


auto_1 = WorkCar(65, 'Red', 'Ford', False)
auto_2 = TownCar(40, 'Black', 'Mazda', False)

auto_1.show_speed()
auto_2.go()