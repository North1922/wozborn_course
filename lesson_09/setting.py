import json
import os
from colorama import Fore


SAVE_FILE = "save.json"

def save(player, monster, turn):
    """
    Сохраняет текущее состояние игры в JSON файл.
    """
    data = {
        "player": {
            "name": player.name,
            "hp": player.hp,
            "damage": player.damage,
            "armor": player.armor
        },
        "monster": {
            "name": monster.name,
            "hp": monster.hp,
            "damage": monster.damage,
            "armor": monster.armor
        },
        "turn": turn
    }
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except PermissionError as error:
        print(f'{Fore.RED}Ошибка:{error}{Fore.RESET}.Проверьте права на запись в файл')

def loading():
    """
    Загружает сохранённую игру из JSON файла, если он существует.
    Возвращает данные для восстановления игры или None, если файла нет или пользователь отказался.
    """
    if not os.path.isfile(SAVE_FILE):
        print(f"{Fore.LIGHTBLUE_EX}Сохранённая игра не найдена.{Fore.RESET}")
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            while True:
                user_input = input(f"{Fore.LIGHTYELLOW_EX}Найдено сохранение.{Fore.RESET} Хотите загрузить игру? (да/нет): ").lower()
                if user_input == "да":
                    print(f"{Fore.LIGHTBLUE_EX}Игра загружена{Fore.RESET}.")
                    return data
                elif user_input == 'нет':
                    print(f"{Fore.LIGHTBLUE_EX}Начинаем новую игру{Fore.RESET}.")
                    return None
                else:
                    print(f'{Fore.RED}Ввели неверные данные{Fore.RESET}. Введите да или нет')

    except json.JSONDecodeError as error:
        print(f'{Fore.RED}Возникла ошибка  {error}{Fore.RESET}')
        while True:
            er = input(f'{Fore.LIGHTYELLOW_EX}Хотите начать новую игру?{Fore.RESET} да/нет').lower()
            if er == 'да':
                break
            elif er == 'нет':
                print(f'{Fore.LIGHTBLUE_EX}Игра завершена{Fore.RESET}')
                exit()
            else:
                print(f'{Fore.RED}Неверное ввели данные{Fore.RESET}.Введите да/нет')
                continue

    except FileNotFoundError as error:
        print(f'{Fore.RED}Возникла ошибка {error}{Fore.RESET}')
        while True:
            er = input(f'{Fore.LIGHTYELLOW_EX}Хотите начать новую игру?{Fore.RESET} да / нет').lower()
            if er == 'да':
                break
            elif er == 'нет':
                print(f'{Fore.LIGHTBLUE_EX}Игра завершена{Fore.RESET}')
                exit()
            else:
                print(f'{Fore.RED}Неверное ввели данные{Fore.RESET}.Введите да/нет')
                continue

    except PermissionError as error:
        print(f'{Fore.RED}Ошибка: {error}{Fore.RESET}')
        while True:
            er = input(f'{Fore.LIGHTYELLOW_EX}Хотите начать новую игру?{Fore.RESET} да/нет').lower()
            if er == 'да':
                break
            elif er == 'нет':
                print(f'{Fore.LIGHTBLUE_EX}Игра завершена{Fore.RESET}')
                exit()
            else:
                print(f'{Fore.RED}Неверное ввели данные{Fore.RESET}.Введите да/нет')
                continue