# from itertools import count

# for el in count(int(input("Первое число - "))):
   # print(el)
   # if el > 1000:
     #   break

from itertools import cycle

i = 0
my_list = [1234, "alalaa", True, 5.345]
for el in cycle(my_list):
    print(el)
    i += 1
    if i > 1000:
        break
