from abc import ABC, abstractmethod
from enum import Enum


class Stats(Enum):
    intelligence = "intelligence"
    strength = "strength"
    dexterity = "dexterity"
    mana = "mana"


class Character(ABC):
    def __init__(
        self,
        name: str,
        max_hp: int,
        intelligence: int,
        strength: int,
        dexterity: int,
        mana: int,
        defense: int,
    ):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._level = 1
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense
        self._is_alive = True

    def die(self):
        self._is_alive = False
        self._hp = 0
        print(f"{self._name} has just died")

    @abstractmethod
    def attack(self):
        raise NotImplementedError

    def take_damage(self, damage: int):
        damage -= self._defense
        if damage > 0:
            self._hp -= damage

        if self._hp <= 0:
            self.die()

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat: str):
        if stat == Stats.intelligence.value:
            self._intelligence += 1
        elif stat == Stats.strength.value:
            self._strength += 1
        elif stat == Stats.dexterity.value:
            self._dexterity += 1
        elif stat == Stats.mana.value:
            self._mana += 1
        else:
            self._defense += 1

    def rest(self):
        self._hp = self._max_hp

    def heal(self, heal_hp: int):
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp


class Paladin(Character):
    def attack(self):
        if self._mana >= 5:
            self._mana -= 5
            return self._strength * 4

        return self._strength

    def shield(self):
        self._defense += 4 + self._level

    def unshield(self):
        self._defense -= 4 + self._level

    def heal_ally(self, ally: Character):
        heal_hp = int(5 + 2 * self._level + 0.5 * self._mana)
        ally._hp += heal_hp
        if ally._hp > ally._max_hp:
            ally._hp = ally._max_hp


class Mage(Character):
    def attack(self):
        if self._mana >= 3:
            self._mana -= 3
            return self._intelligence * 3 + 4

        return 0

    def fireball(self):
        if self._mana >= 5:
            self._mana -= 5
            return self._intelligence * 2 + 3

        return 0

    def heal_ally(self, ally: Character):
        heal_hp = 3 + self._level + 3 * self._intelligence
        ally._hp += heal_hp
        if ally._hp > ally._max_hp:
            ally._hp = ally._max_hp


class Warrior(Character):
    def attack(self):
        return self._strength * 4 + 3

    def power_strike(self, enemies: list[Character]):
        for enemy in enemies:
            if enemy._level < self._level:
                enemy.die()


class Rogue(Character):
    def attack(self):
        return self._strength + self._level


# 1. Створюємо героїв різних класів
pala = Paladin("Артур", 120, 10, 15, 8, 20, 10)
mage = Mage("Гендальф", 80, 20, 5, 10, 30, 5)
warrior = Warrior("Конан", 150, 5, 18, 12, 0, 15)
rogue = Rogue("Еціо", 90, 8, 12, 20, 10, 8)

print("--- ТЕСТУВАННЯ ВМІНЬ ---")

# ТЕСТ ПАЛАДИНА (Щит та лікування)
print(f"Захист Паладина до щита: {pala._defense}")
pala.shield()
print(f"Захист Паладина після щита: {pala._defense}")

# ТЕСТ МАГА (Атака магією та лікування союзника)
print(f"\nHP Воїна до лікування Магом: {warrior._hp}")
warrior._hp -= 50  # Трохи поранимо воїна
mage.heal_ally(warrior)
print(f"HP Воїна після лікування Магом: {warrior._hp}")

# ТЕСТ БОЮ (Метод attack всередині take_damage)
print(f"\n--- Бій: {warrior._name} б'є {rogue._name} ---")
print(f"HP Розбійника до удару: {rogue._hp}")
rogue.take_damage(warrior.attack())
print(f"HP Розбійника після удару: {rogue._hp}")

# ТЕСТ ВОЇНА (Power Strike)
print(f"\n--- {warrior._name} використовує Power Strike на Мага ---")
warrior.power_strike([mage])
# Якщо рівень мага (1) < рівня воїна (1), він не помре (бо вони рівні),
# але давай піднімемо воїну рівень
warrior.level_up()
warrior.power_strike([mage])  # Тепер маг має померти

# ТЕСТ ВІДПОЧИНКУ ТА СТАТІВ
print(f"\nСтати до прокачки: {rogue._dexterity}")
rogue.increase_stat(Stats.dexterity.value)  # Використовуємо твій Enum
print(f"Стати після прокачки: {rogue._dexterity}")

rogue.rest()
print(f"HP Розбійника після відпочинку: {rogue._hp}")
