import time
import random
from colorama import Fore

def move():
    global move_num
    move_num += 1


def random_stats():#функция которая генерирует урон и защиту
    damage = random.randint(1,20)
    armor = random.randint(1,20)
    return damage, armor

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
        choice = input(Fore.LIGHTYELLOW_EX + 'Введите ваше действие:' + Fore.RESET + ' Атака/Защита').lower()
        print(Fore.BLUE + "----------------------" + Fore.RESET)
        if choice == 'атака':
            print(Fore.GREEN + '*Вы Атакуете*' + Fore.RESET)
            return choice
        elif choice == 'защита':
            print(Fore.LIGHTBLUE_EX + '*Вы Защищаетесь*' + Fore.RESET)
            return choice
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
                monster_hp = player_attack(random.randint(0,player_damage), monster_hp)# нанесение урона монстру. Функция random.randint(0, player_damage) реализована для рандомной генерации урона.
                player_hp = monster_attack(random.randint(0,monster_damage), player_hp)#нанесекние урона игроку. Функция random.randint(0, player_damage) реализована для рандомной генерации урона.#проверка здоровья игрока и монстра после атак
                if check_result(player_hp, monster_hp):  # Проверка результата
                    break

            case 'атака', 'защита':
                monster_hp = player_attack(random.randint(0,player_damage), monster_hp, random.randint(0,monster_armor))#нанесение урона монстру#проверка здоровья игрока и монстра после атак
                if check_result(player_hp, monster_hp):  # Проверка результата
                    break

            case 'защита', 'атака':
                player_hp = monster_attack(random.randint(0,monster_damage), player_hp, random.randint(0,player_armor))#нанесение урона человеку#проверка здоровья игрока и монстра после атак
                if check_result(player_hp, monster_hp):  # Проверка результата
                    break

            case 'защита', 'защита':
                print("**Стоите и смотрите друг на друга прикрывшись щитом**")
                if check_result(player_hp, monster_hp):  # Проверка результата
                    break


                    # использование рандомной генерации урона и защиты при помощи random.randint обусловлено тем что во время
            # драки акатующий не всегда может нанести максимальный урон , например он может промахнуться или попасть в
            # скользь. По тому же принципу выбрали random.randint длф генерации защиты. Когда защищается человек или
            # монстр не всегда защита будем максимально эффективна , так как можно поздно среагировать на атаку
            # соперника или соперник может атаковать через ложную атаку и т.д

print(Fore.LIGHTMAGENTA_EX + "Добро пожаловать в игру про драки с монстром!" + Fore.RESET)
print(Fore.BLUE + "**********************" + Fore.RESET)
player_hp = 30# Игрок
monster_hp = 30# Монстр
move_num = 0 # счётчик хода
print(Fore.LIGHTGREEN_EX + 'Создаю Персонажей....' + Fore.RESET)
print(Fore.BLUE + "**********************" + Fore.RESET)
time.sleep(1)
monster_damage, monster_armor = random_stats()
print(f'{Fore.LIGHTGREEN_EX}---Монстр создан--- {Fore.RESET}||Здоровье:{monster_hp}. Защита:{monster_armor}. Урон:{monster_damage}||')
time.sleep(0.5)
player_damage, player_armor = random_stats()
print(f'{Fore.LIGHTGREEN_EX}---Игрок создан--- {Fore.RESET}||Здоровье:{player_hp}. Защита:{player_armor}. Урон:{player_damage}||')
time.sleep(1)
print(Fore.BLUE + "**********************" + Fore.RESET)

fight(player_hp, player_damage, player_armor, monster_hp, monster_damage, monster_armor)
print(move_num)