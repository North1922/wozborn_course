import time

from monster import Monster
from player import Player
from setting import save, loading

def main():
    saved_data = loading()# Проверяем, есть ли сохранение

    if saved_data:# Загружаем игру из сохранения
        player = Player(
            name=saved_data["player"]["name"],
            hp=saved_data["player"]["hp"],
            damage=saved_data["player"]["damage"],
            armor=saved_data["player"]["armor"]
        )
        monster = Monster(
            name=saved_data["monster"]["name"],
            hp=saved_data["monster"]["hp"],
            damage=saved_data["monster"]["damage"],
            armor=saved_data["monster"]["armor"]
        )
        turn = saved_data["turn"]
    else:
        # Начинаем новую игру
        player = Player(name="Герой", hp=100, damage=20, armor=5)
        monster = Monster(name="Монстр", hp=100, damage=15, armor=3)
        turn = 1


    while player.is_alive() and monster.is_alive(): # Основной игровой цикл работает до тех пор пока монстр или игрок живы
        print(f"\n*** Ход {turn} ***")
        player.display_health()
        monster.display_health()
        print('**********************')
        choice = input("Выберите ваше действие: атака/защита/выход (для сохранения прогресса и выхода из игры)").lower() # Ход игрока

        if choice == "атака":  # Атака
            player.attack(monster)
            time.sleep(1)
        elif choice == "защита":  # Защита
            print(f"{player.name} защищается.")
            time.sleep(1)
        elif choice == "выход":  # Выход
            print("выход")
            save(player, monster, turn)
            break
        else:
            print("Неверно ввели действие. Введите: атака / защита / выход")
            continue
        if not monster.is_alive():# Проверяем, жив ли монстр после хода игрока
            print(f"{monster.name} побежден!")
            break

        print(f"\nХод {monster.name}:")# Ход монстра
        time.sleep(1)
        monster.attack(player)
        time.sleep(1)

        if not player.is_alive():# Проверяем, жив ли игрок после хода монстра
            print(f"{player.name} побежден!")
            break

        save(player, monster, turn)# Сохраняем игру после каждого хода
        turn += 1

    print("\n--- Игра окончена ---")
    player.display_health()
    monster.display_health()

if __name__ == "__main__":
    main()