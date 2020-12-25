
my_list = [7, 56.9, "hello", True, 5+6j]
# size = len(my_list)
# while size > 0:
   # print(type(my_list[0]))
   # my_list.pop(0)
# IndexError: list index out of range
   # print(str(my_list[0]) + " - " + type(my_list[0]))
   # my_list.pop(0)
# can only concatenate str (not "type") to str
for i in range(len(my_list)):
    print(type(my_list[i]))
# Почему не работает без range(len(..))?