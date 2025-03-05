
herbs = float(input("Введите количество травы: "))
crystals = float(input("Введите количество кристаллов: "))
water = float(input("Введите количество воды: "))
fire_dust = float(input("Введите количество огненной пыли: "))
moonlight = float(input("Введите количество лунного света: "))

magic_power = (herbs * 0.5) + (crystals * 1.5) + (water * 0.8) + (fire_dust * 1.0) + (moonlight * 1.2)

total_ingredients = herbs + crystals + water + fire_dust + moonlight
bonus = 20 * (total_ingredients > 150)  # если в скобочках значение TRUE то true = 1 , false = 0.
# Таким образом получилась проверка на бонус , если общее кол-во ингридиентов больше 150
magic_power += bonus

# Вывод результата
print(f"Магическая сила зелья: {magic_power}")