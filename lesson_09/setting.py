
import json
import os

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
        print(f"TEST-Игра сохранена в файл {SAVE_FILE}.-TEST")
    except PermissionError as error:
        print(f'Ошибка:{error}.Проверьте права на запись в файл')

def loading():
    """
    Загружает сохранённую игру из JSON файла, если он существует.
    Возвращает данные для восстановления игры или None, если файла нет или пользователь отказался.
    """
    if not os.path.isfile(SAVE_FILE):
        print("Сохранённая игра не найдена.")
        return None

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            while True:
                user_input = input("Найдено сохранение. Хотите загрузить игру? (да/нет): ").lower()
                if user_input == "да":
                    print("Игра загружена.")
                    return data
                elif user_input == 'нет':
                    print("Начинаем новую игру.")
                    return None
                else:
                    print('Ввели неверные данные. Введите да или нет')

    except json.JSONDecodeError as error:
        print(f'Возникла ошибка  {error}')
        while True:
            er = input(f'Хотите начать новую игру? да/нет').lower()
            if er == 'да':
                break
            elif er == 'нет':
                print(f'Игра завершена')
                exit()
            else:
                print(f'Неверное ввели данные.Введите да/нет')
                continue

    except FileNotFoundError as error:
        print(f'Возникла ошибка {error}')
        while True:
            er = input(f'Хотите начать новую игру? да / нет').lower()
            if er == 'да':
                break
            elif er == 'нет':
                print(f'Игра завершена')
                exit()
            else:
                print(f'Неверное ввели данные.Введите да/нет')
                continue

    except PermissionError as error:
        print(f'Ошибка: {error}')
        while True:
            er = input(f'Хотите начать новую игру? да/нет').lower()
            if er == 'да':
                break
            elif er == 'нет':
                print(f'Игра завершена')
                exit()
            else:
                print(f'Неверное ввели данные.Введите да/нет')
                continue