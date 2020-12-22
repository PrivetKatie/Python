customer_age = int(input("Введите ваш возраст!"))
allow_age = 18
difference = int(18 - customer_age)
if(customer_age >= allow_age):
    name = input("Введите ваше имя!")
    print("Добро пожаловать " + name + "!")
elif(customer_age < allow_age):
    if(difference == 1):
        print("Извините, вы еще очень юны. Возвращайтесь через " + str(difference) + " год!")
    elif(difference > 1 and difference < 5):
        print("Извините, вы еще очень юны. Возвращайтесь через " + str(difference) + " годa!")
    else:
        print("Извините, вы еще очень юны. Возвращайтесь через " + str(difference) + " лет!")