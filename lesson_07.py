import time
import random
from colorama import Fore



def random_stats():#функция которая генерирует урон и защиту
    damage = random.randint(1,20)
    armor = random.randint(1,20)
    return damage, armor

def check_result(player_hp: int, monster_hp: int): #функция проверяет остатки здоровья
    if player_hp <= 0:
        print(Fore.RED + "Тебя убили!" + Fore.RESET)
        print(Fore.GREEN + 'Монстр Побеждает!' + Fore.RESET)
        exit()
    elif monster_hp <= 0:
        print(Fore.RED + "Монстр убит!" + Fore.RESET)
        print(Fore.GREEN + "Ты побеждаешь" + Fore.RESET)
        exit()
    else:
        print(Fore.BLUE + "**********************" + Fore.RESET)
        print(f'Твоё здоровье: {player_hp} ')
        print(f'Здоровье монстра: {monster_hp} ')
        print(Fore.BLUE + "**********************" + Fore.RESET)


def monster_attack(monster_damage: int, player_hp: int, player_armor = 0):# функция атаки монстра , возвращает кол-во hp
    # человека которое останется после атаки
    #print('Монстр атакует')
    player_hp = player_hp - max(monster_damage - player_armor, 0)# функцию max применил для того что бы избежать
    # отрицательного значения, без этой функции иногда если броня была больше чем урон происходило
    # увеличение урона а не уменьшение
    return player_hp

def player_attack(player_damage: int, monster_hp: int, monster_armor: int = 0): # функция атаки человека , возвращает кол-во
    # hp монстра которое останется после атаки человека
    #print('Человек атакует')
    monster_hp = monster_hp - max(player_damage - monster_armor, 0)# функцию max применил для того что бы избежать
    # отрицательного значения, без этой функции иногда если броня была больше чем урон происходило
    # увеличение урона а не уменьшение
    return monster_hp

def player_choice(): #функция выбора действия игрока
    while True:
        choice = input(Fore.LIGHTYELLOW_EX + 'Введите ваше действие:' + Fore.RESET + ' Атака/Защита').lower()
        if choice == 'атака':
            print(Fore.LIGHTGREEN_EX + '*Вы Атакуете*' + Fore.RESET)
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
        print(Fore.RED + '*Монстр Атакует*' + Fore.RESET)
        return choice


print(Fore.LIGHTMAGENTA_EX + "Добро пожаловать в игру про драки с монстром!" + Fore.RESET)
print(Fore.BLUE + "**********************" + Fore.RESET)
player_hp = 100# Игрок
monster_hp = 100# Монстр
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

while True: #Основной цикл при помощи которого игра работает
    player_fight = player_choice()# переменная принимает в себя значение функции которая возвращает
    # действие которое выбрал пользователь
    monster_fight = monster_choice()# переменная принимает в себя значение функции которая возвращает
    # сгенерированое действие монстра
    if player_fight == 'атака' and monster_fight == 'атака':
        monster_hp = player_attack(player_damage, monster_hp)#функция атаки человека , возвращает кол-во hp
    # человека которое останется после атаки
        player_hp = monster_attack(monster_damage, player_hp)#функция атаки монстра , возвращает кол-во hp
    # человека которое останется после атаки
        check_result(player_hp, monster_hp)#функция проверяет остатки здоровья

    elif player_fight == 'атака' and monster_fight == 'защита':
        monster_hp = player_attack(player_damage, monster_hp, monster_armor)#функция атаки человека , возвращает кол-во hp
    # человека которое останется после атаки
        check_result(player_hp, monster_hp)#функция проверяет остатки здоровья

    elif player_fight == 'защита' and monster_fight == 'атака':
        player_hp = monster_attack(monster_damage, player_hp, player_armor)#функция атаки монстра , возвращает кол-во hp
    # человека которое останется после атаки
        check_result(player_hp, monster_hp)#функция проверяет остатки здоровья

    elif player_fight == 'защита' and monster_fight == 'защита':
        print("**Стоите и смотрите друг на друга прикрывшись щитом**")
        check_result(player_hp, monster_hp)#функция проверяет остатки здоровья