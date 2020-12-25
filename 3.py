# seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
# user_season = int(input("Введите номер месяца: "))
# if user_season > 2 and user_season < 6:
 #    print("Это " + str(seasons.get(2)))
# elif user_season > 5 and user_season < 9:
  #   print("Это " + str(seasons.get(3)))
# elif user_season > 8 and user_season < 12:
 #    print("Это " + str(seasons.get(4)))
# else:
 #    print("Это " + str(seasons.get(1)))

seasons = ["зима", "весна", "лето", "осень"]
user_season = int(input("Введите номер месяца: "))
if user_season > 2 and user_season < 6:
    print("Это " + str(seasons[1]))
elif user_season > 5 and user_season < 9:
    print("Это " + str(seasons[2]))
elif user_season > 8 and user_season < 12:
    print("Это " + str(seasons[3]))
else:
    print("Это " + str(seasons[0]))

    # работает и через список и через словарь