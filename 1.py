import colorama
import time


class TrafficLight:

    __color = ["Красный", "Желтый", "Зеленый"]
    make_color = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN]
    time = [7, 2, 5]

    def running(self):
        i = 0
        while i < len(self.__color):
            print(f'{self.make_color[i]} {self.__color[i]} сигнал сфетофора!')
            time.sleep(self.time[i])
            i += 1


traffic_light_1 = TrafficLight()

# while True: чтобы сделать бесконечный
traffic_light_1.running()