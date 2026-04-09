from abc import ABC, abstractmethod


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

    @abstractmethod
    def attack(self):
        raise NotImplementedError

    def take_damage(self, damage: int):
        damage -= self._defense
        if damage > 0:
            self._hp -= damage

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat: str):
        if stat == "intelligence":
            self._intelligence += 1
        elif stat == "strength":
            self._strength += 1
        elif stat == "dexterity":
            self._dexterity += 1
        elif stat == "mana":
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
        self._defense -= 4 - self._level

    def heal_ally(self, ally: Character):
        heal_hp = 5 + 2 * self._level + 0.5 * self._mana
        ally._hp += heal_hp
        if ally._hp > self._max_hp:
            ally._hp = self._max_hp


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
        if ally._hp > self._max_hp:
            ally._hp = self._max_hp
