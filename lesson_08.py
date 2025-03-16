import time
import random
from json import JSONDecodeError
from colorama import Fore
import json
import os
import pickle



def new_game(data_conservation: dict) -> dict:
    print(Fore.LIGHTGREEN_EX + 'Создаю Персонажей....' + Fore.RESET)
    print(Fore.BLUE + "**********************" + Fore.RESET)

    data_conservation['player_hp'] = 100
    data_conservation['player_damage'] = random_stats()
    data_conservation['player_armor'] = random_stats()
    data_conservation['monster_hp'] = 100
    data_conservation['monster_damage'] = random_stats()
    data_conservation['monster_armor'] = random_stats()
    data_conservation['move_num'] = 0
    print("Монстр создан: " +
          "Здоровье - " + str(data_conservation['monster_hp'])+
          ". Урон - " + str(data_conservation['monster_damage']) +
          ". Защита - " + str(data_conservation['monster_armor']))
    time.sleep(0.5)
    print("Игрок создан: " +
          "Здоровье - " + str(data_conservation['player_hp']) +
          ". Урон - " + str(data_conservation['player_damage']) +
          ". Защита - " + str(data_conservation['player_armor']))
    return data_conservation


def loading(file_name:str) -> dict | None:
    """Проверка наличия сохранения. В случае если сохранение имеется старт игры из места сохранения
        Args:
            file_name (str) : название файла который будет загружен и из него будут использованы данные для старта игры.
        Returns:
            file_log (dict) : словарь в котором находятся данные их используем для записи в переменные
    """
    if os.path.isfile(file_name):
        try:
            while True:
                choice = input('Найдено сохранение. Хотите загрузить? да/нет').lower()
                if choice == 'да':
                    with open(file_name, 'r') as f:#тело функции load() написали здесь для того что бы проще тестировать функционал
                        file_log = json.load(f)
                        return file_log
                elif choice == 'нет':
                    break
                else:
                    print('Не верно ввели ответ. Введите да или нет')
        except json.JSONDecodeError as error:
            print(f'Возникла ошибка {error}')
            while True:
                er = input(f'Хотите начать новую игру? да/нет').lower()
                if er == 'да':
                    break
                elif er == 'нет':
                    print('Игра завершена')
                    exit()
                else:
                    print('Неверное ввели данные. Введите да/нет')
                    continue
        except FileNotFoundError as error:
            print(f'Возникла ошибка{error}')
            while True:
                er = input('Хотите начать новую игру? да/нет').lower()
                if er == 'да':
                    break
                elif er == 'нет':
                    print('Игра завершена')
                    exit()
                else:
                    print('Неверное ввели данные. Введите да/нет')
                    continue
        except PermissionError as error:
            print(f'Ошибка: {error}')
            while True:
                er = input('Хотите начать новую игру? да/нет').lower()
                if er == 'да':
                    break
                elif er == 'нет':
                    print('Игра завершена')
                    exit()
                else:
                    print('Неверное ввели данные. Введите да/нет')
                    continue
    else:
        print('Не обнаружено файла с сохранением.')
        file_log = None
        return file_log


def save(data: dict, file_name:str):
    """Функция для создания файла сохранения и записи в него данных
        Args:
            data (dict) : словарь с параметрами который будет сохранён в json.
            file_name (str) : название файла который будет создан и в него сохранятся данные из data.
        Returns:
            -
    """
    try:
        with open(file_name,'w') as save_file:#открываем файл на запись, если его нет то создаётся файл с названием
            # хранящимся в переменной file_name
            json.dump(data, save_file) #dump() преобразует объект Python в строку JSON и записывает её в файл
    except PermissionError as error:
        print(f'Ошибка: {error}. Проверьте права на запись в файл')




def move():
    """функция подсчёта хода"""
    global move_num
    data_conservation['move_num'] += 1


def random_stats():#функция которая генерирует урон и защиту
    """Генерирует урон и защиту"""
    num = random.randint(1,20)
    return num

def check_result(player_hp: int, monster_hp: int): #функция проверяет остатки здоровья
    if player_hp <= 0:
        move()
        print(Fore.RED + "Тебя убили!" + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + '!!!МОНСТР ПОБЕЖДАЕТ!!! Игра закончена' + Fore.RESET)
        return True
    elif monster_hp <= 0:
        move()
        print(Fore.RED + "Монстр убит!" + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + "!!!ТЫ ПОБЕЖДАЕШЬ!!! Игра закончена" + Fore.RESET)
        return True
    else:
        move()
        print(Fore.BLUE + "----------------------" + Fore.RESET)
        print(f'Твоё здоровье: {player_hp} ')
        print(f'Здоровье монстра: {monster_hp} ')
        print(Fore.BLUE + "**********************" + Fore.RESET)
        save(data_conservation, file_name)
        """через контекстный менеджер записываем логи в файл в этом блоке и так же рассмотреть
         вариант запись логов при завершении игры в результате победы игрока или монстра"""


def monster_attack(monster_damage: int, player_hp: int, player_armor = 0):# функция атаки монстра , возвращает кол-во hp
    # человека которое останется после атаки
    #print('Монстр атакует')
    player_hp = player_hp - max(monster_damage - player_armor, 0)
    print(f'|||Монстр нанёс: {Fore.RED}{max(monster_damage - player_armor, 0)}{Fore.RESET} урона|||')# функцию max применил для того что бы избежать
    # отрицательного значения, без этой функции иногда если броня была больше чем урон происходило
    # увеличение урона а не уменьшение
    return player_hp

def player_attack(player_damage: int, monster_hp: int, monster_armor: int = 0): # функция атаки человека , возвращает кол-во
    # hp монстра которое останется после атаки человека
    #print('Человек атакует')
    monster_hp = monster_hp - max(player_damage - monster_armor, 0)
    print(f'|||Ты нанёс:{Fore.RED} {max(player_damage - monster_armor, 0)} {Fore.RESET}урона|||')# функцию max применил для того что бы избежать
    # отрицательного значения, без этой функции иногда если броня была больше чем урон происходило
    # увеличение урона а не уменьшение
    return monster_hp


def player_choice(): #функция выбора действия игрока
    while True:
        choice = input(Fore.LIGHTYELLOW_EX + 'Введите ваше действие:' + Fore.RESET + ' Атака/Защита/Выход (для сохранения прогресса и выхода из игры)').lower()
        print(Fore.BLUE + "----------------------" + Fore.RESET)
        if choice == 'атака':
            print(Fore.GREEN + '*Вы Атакуете*' + Fore.RESET)
            return choice
        elif choice == 'защита':
            print(Fore.LIGHTBLUE_EX + '*Вы Защищаетесь*' + Fore.RESET)
            return choice
        elif choice == 'выход':
            save(data_conservation,file_name)
            print('Игра завершена.')
            exit()
        else:
            print(Fore.LIGHTRED_EX + 'Такого варианта нет!' + Fore.RESET)

def monster_choice(): # функция которая генерирует рандомно действия монстра
    variants = ["защита", "атака"]
    choice = random.choice(variants)
    if choice == 'защита':
        print(Fore.MAGENTA + '*Монстр Защищается*' + Fore.RESET)
        return choice
    elif choice == 'атака':
        print(Fore.MAGENTA + '*Монстр Атакует*' + Fore.RESET)
        return choice

def fight(player_hp, player_damage, player_armor, monster_hp, monster_damage, monster_armor ):#функция которая реализует бой , между игроком и монстром
    while  True:
        player_fight = player_choice()#в переменную помещаем действие которое выбрал игрок
        monster_fight = monster_choice()#в переменную помещаем рендомно сгенерированное действие монстра
        match player_fight, monster_fight:# сравниваем значения переменных player_fight и monster_fight через match case
            case 'атака' , 'атака':
                data_conservation['monster_hp'] = player_attack(random.randint(0,data_conservation['player_damage']), data_conservation['monster_hp'])# нанесение урона монстру. Функция random.randint(0, player_damage) реализована для рандомной генерации урона.
                data_conservation['player_hp'] = monster_attack(random.randint(0,data_conservation['monster_damage']), data_conservation['player_hp'])#нанесекние урона игроку. Функция random.randint(0, player_damage) реализована для рандомной генерации урона.#проверка здоровья игрока и монстра после атак
                if check_result(data_conservation['player_hp'], data_conservation['monster_hp']):  # Проверка результата
                    break

            case 'атака', 'защита':
                data_conservation['monster_hp'] = player_attack(random.randint(0,data_conservation['player_damage']), data_conservation['monster_hp'], random.randint(0,data_conservation['monster_armor']))#нанесение урона монстру#проверка здоровья игрока и монстра после атак
                if check_result(data_conservation['player_hp'], data_conservation['monster_hp']):  # Проверка результата
                    break

            case 'защита', 'атака':
                data_conservation['player_hp'] = monster_attack(random.randint(0,data_conservation['monster_damage']), data_conservation['player_hp'], random.randint(0,data_conservation['player_armor']))#нанесение урона человеку#проверка здоровья игрока и монстра после атак
                if check_result(data_conservation['player_hp'], data_conservation['monster_hp']):  # Проверка результата
                    break

            case 'защита', 'защита':
                print("**Стоите и смотрите друг на друга прикрывшись щитом**")
                if check_result(data_conservation['player_hp'], data_conservation['monster_hp']):  # Проверка результата
                    break


                    # использование рандомной генерации урона и защиты при помощи random.randint обусловлено тем что во время
            # драки акатующий не всегда может нанести максимальный урон , например он может промахнуться или попасть в
            # скользь. По тому же принципу выбрали random.randint длф генерации защиты. Когда защищается человек или
            # монстр не всегда защита будем максимально эффективна , так как можно поздно среагировать на атаку
            # соперника или соперник может атаковать через ложную атаку и т.д


print(Fore.LIGHTMAGENTA_EX + "Добро пожаловать в игру про драки с монстром!" + Fore.RESET)
print(Fore.BLUE + "**********************" + Fore.RESET)
file_name = 'save.json' #название файла который будет использоваться для сохранения промежуточных данных
file_log = loading(file_name)

data_conservation = {'player_hp': 0,
                     'player_damage': 0,
                     'player_armor': 0,
                     'monster_hp': 0,
                     'monster_damage': 0,
                     'monster_armor': 0,
                     'move_num': 0}


if file_log is None:
    new_game(data_conservation)
else:
    data_conservation['player_hp'] = file_log['player_hp']
    data_conservation['player_damage'] = file_log['player_damage']
    data_conservation['player_armor'] = file_log['player_armor']
    data_conservation['monster_hp'] = file_log['monster_hp']
    data_conservation['monster_damage'] = file_log['monster_damage']
    data_conservation['monster_armor'] = file_log['monster_armor']
    data_conservation['move_num'] = file_log['move_num']

    print('Игра начинается с места сохранения...')
    print('Твои характеристики: ' +
          'Здоровье: ' + str(data_conservation['player_hp']) +
          '. Урон: ' + str(data_conservation['player_damage']) +
          '. Защита: ' + str(data_conservation['player_armor']) + '.')
    print('Характеристики монстра: ' +
          'Здоровье: ' + str(data_conservation['monster_hp']) +
          '. Урон: ' + str(data_conservation['monster_damage']) +
          '. Защита: ' + str(data_conservation['monster_armor']) + '.')


fight(data_conservation['player_hp'], data_conservation['player_damage'], data_conservation['player_armor'], data_conservation['monster_hp'], data_conservation['monster_damage'], data_conservation['monster_armor'])