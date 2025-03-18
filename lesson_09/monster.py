import random

from colorama import Fore

class Monster:
    """
    Класс для монстра.
    """
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, target):
        """
        Атака цели с учетом случайного урона и защиты.
        """
        damage_dealt = max(0, random.randint(0, self.damage) - random.randint(0, target.armor))
        print(f'{Fore.LIGHTYELLOW_EX}------------------------{Fore.RESET}')
        print(f"{self.name} {Fore.RED}атакует{Fore.RESET} {target.name}!")
        print(f'{Fore.LIGHTYELLOW_EX}------------------------{Fore.RESET}')
        target.take_damage(damage_dealt)

    def take_damage(self, amount):
        """
        Получение урона.
        """
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name}{Fore.GREEN} получает {amount} урона.{Fore.RESET} Осталось здоровья: {self.hp}")

    def display_health(self):
        """
        Отображение текущего здоровья.
        """
        print(f"{self.name}:{Fore.CYAN} Здоровье{Fore.RESET} = {self.hp}")

    def is_alive(self):
        """
        Проверка, жив ли персонаж.
        """
        return self.hp > 0

    def choice(self):
        variants = ["защита", "атака"]
        choice = random.choice(variants)
        if choice == 'защита':
            print('*Монстр Защищается*')
            return choice
        elif choice == 'атака':
#             print('*Монстр Атакует*')
            return choice
