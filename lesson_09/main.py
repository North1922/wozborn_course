import random
import time
from colorama import Fore

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
        player = Player(name="Герой", hp=100, damage = random.randint(1,20), armor = random.randint(1,20))
        monster = Monster(name="Монстр", hp=100, damage = random.randint(1,20), armor = random.randint(1,20))
        turn = 1


    while player.is_alive() and monster.is_alive(): # Основной игровой цикл работает до тех пор пока монстр или игрок живы
        print(f"{Fore.LIGHTMAGENTA_EX}*** Ход {turn} ***{Fore.RESET}")
        print(f'{Fore.LIGHTYELLOW_EX}------------------------{Fore.RESET}')
        player.display_health()
        monster.display_health()
        print(f'{Fore.LIGHTYELLOW_EX}------------------------{Fore.RESET}')
        choice = input(f"{Fore.LIGHTYELLOW_EX}Выберите ваше действие:{Fore.RESET} атака/защита/выход (для сохранения прогресса и выхода из игры)").lower() # Ход игрока



        if choice == "атака":  # Атака
            player.attack(monster)
        elif choice == "защита":  # Защита
            print(f"*{player.name} защищается*.")
        elif choice == "выход":  # Выход
            print("выход")
            save(player, monster, turn)
            break
        else:
            print(f"{Fore.RED}Неверно ввели действие.{Fore.RESET} Введите: атака / защита / выход")
            continue
        if not monster.is_alive():# Проверяем, жив ли монстр после хода игрока
            print(f"{monster.name} побежден!")
            break


        if monster.choice() == 'атака':
            monster.attack(player)

        if not player.is_alive():# Проверяем, жив ли игрок после хода монстра
            print(f"{player.name} побежден!")
            break

        save(player, monster, turn)# Сохраняем игру после каждого хода
        turn += 1

    print(f"{Fore.BLUE}--- Игра окончена ---{Fore.RESET}")
    player.display_health()
    monster.display_health()

if __name__ == "__main__":
    main()