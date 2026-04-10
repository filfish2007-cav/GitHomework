from abc import ABC, abstractmethod
from enum import Enum

class Sounds(Enum):
    gav = "гав"
    myav = "мяу"

class SatietyParamError(Exception):
    pass

class EnergyParamError(Exception):
    pass




class Pet(ABC):
    def __init__(self, name: str, satiety: int = 50, energy: int = 50):
        self._name = name
        self._check_stats(satiety, energy)
        self._satiety = satiety
        self._energy = energy

    def sleep(self):
        self._energy = 100
        return f"Your pet: {self._name} took a nap and his energy now {self._energy}"

    def eat(self, food_amount: int):
        self._satiety += food_amount
        if self._satiety > 100:
            self._satiety = 100
        return f"Your pet: {self._name} had a meal and his satiety now {self._satiety}"

    @abstractmethod
    def play(self, activity_level: int):
        if self._energy < 0:
            self._energy = 0
        if self._satiety < 0:
            self._satiety = 0

    def make_sound(self):
        pass

    @staticmethod
    def _check_stats(en,sat):
        if en < 0 or en > 100:
            raise EnergyParamError("energy should be between 0 and 100")
        if sat < 0 or sat > 100:
            raise SatietyParamError("satiety should be between 0 and 100")

class Cat(Pet):
    def play(self, activity_level: int):
        if self._satiety > 60:
            self._energy -= 2 * activity_level
            self._satiety -= activity_level
            super().play(activity_level)

            return (f"Your Cat {self._name} was running a lot so his energy now {self._energy} "
                    f" and his satiety is at {self._satiety}")

        return (f"Your Cat {self._name} is too"
                f" hungry to play: {self._satiety} - (60 required)")

    def make_sound(self):
        return Sounds.myav.value

    def catch_mouse(self):
        if self._energy > 30 and self._satiety > 40:
            return (f"Your Cat {self._name} has just caught a mouse"
                    f" and playing with it")

        elif self._energy > 30:
            return (f"Your Cat {self._name} has just caught a mouse"
                    f" and ate it")

        return (f"Your Cat {self._name} is too "
                f" tired to catch a mouse: {self._energy} - (30 required)")

class Dog(Pet):
    def play(self, activity_level: int):
        if self._satiety > 15:
            self._energy -= activity_level // 2
            self._satiety -= activity_level // 2
            super().play(activity_level)

            return (f"Your Dog {self._name} was running a lot so his energy now {self._energy} "
                    f" and his satiety is at {self._satiety}")

        return (f"Your Dog {self._name} is too"
                f" hungry to play: {self._satiety} - (15 required)")

    def make_sound(self):
        return Sounds.gav.value

    def fetch_ball(self):
        if self._satiety > 10:
            self._energy -= 5
            super().play(0)
            return (f"Your Dog {self._name} has just caught a ball"
                    f" his energy now {self._energy} ")

        return f"Your Dog {self._name} is too hungry to catch a ball"

try:
    barsik = Dog("Barsik")
    asik = Cat("Asik")
except SatietyParamError:
    print("Satiety param error")
except EnergyParamError:
    print("Energy param error")


print(barsik.eat(5))
print(barsik.fetch_ball())
print(barsik.make_sound())
print(barsik.sleep())
print(barsik.play(201))
print(barsik.play(202))

print(asik.eat(5))
print(asik.catch_mouse())
print(asik.make_sound())
print(asik.sleep())
print(asik.play(201))
print(asik.play(202))












