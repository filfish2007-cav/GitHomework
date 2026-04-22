# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_
# level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off

from abc import ABC
from enum import Enum
from uuid import uuid4


class RoboStatus(Enum):
    off = "off"
    on = "on"


class Robot(ABC):
    def __init__(
        self,
        name: str | None = None,
        battery_level: int = 100,
        status: RoboStatus = RoboStatus.off,
    ):
        if name is None:
            name = str(uuid4())

        self._name = name
        self._battery_level = battery_level
        self._status = status

    def show_info(self):
        print(f"Robot: {self._name}")
        print(f"Battery Level: {self._battery_level}")
        print(f"Status: {self._status}")

    def charge(self):
        self._battery_level = 100

    def turn_on(self):
        self._status = RoboStatus.on

    def turn_off(self):
        self._status = RoboStatus.off


robot1 = Robot()
robot1.show_info()
robot1.turn_on()
robot1.show_info()


class CleaningMode(Enum):
    dry = "dry"
    wet = "wet"


class CleaningRobot(Robot):
    def __init__(
        self,
        cleaning_mode: CleaningMode,
        name: str | None = None,
        battery_level: int = 100,
        status: RoboStatus = RoboStatus.off,
        dust_capacity: int = 0,
        water_capacity: int = 100,
    ):
        super().__init__(name, battery_level, status)
        self._dust_capacity = dust_capacity
        self._water_capacity = water_capacity
        self._cleaning_mode = cleaning_mode

    def show_info(self):
        super().show_info()
        print(f"Cleaning Mode: {self._cleaning_mode}")
        print(f"Dust Capacity: {self._dust_capacity}")
        print(f"Water Capacity: {self._water_capacity}")

    def turn_on(self):
        if self._dust_capacity >= 100:
            print("dust capacity exceeded or full")
            return

        if self._water_capacity <= 0 and self._cleaning_mode == CleaningMode.wet:
            print("water capacity is empty")
            return

        super().turn_on()

    def empty_dust_bin(self):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        self._dust_capacity = 0

    def fill_water(self):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        if self._cleaning_mode == CleaningMode.wet:
            self._water_capacity = 100

    def swap_dust(self):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        if self._cleaning_mode == CleaningMode.wet:
            self._cleaning_mode = CleaningMode.dry
        else:
            self._cleaning_mode = CleaningMode.wet

    def clean(self, energy: int, dust: int, water=None):
        if self._status == RoboStatus.off:
            print("Robot is not turned on")
            return

        if self._battery_level - energy < 0:
            print("Not enough battery capacity")
            return

        if self._dust_capacity + dust > 100:
            print("dust capacity exceeded or full")
            return

        if self._cleaning_mode == CleaningMode.wet:
            if water is None:
                print("you must specify a water usage")
                return

            if self._dust_capacity - abs(water) < 0:
                print("Not enough water capacity")
                return

            self._dust_capacity += dust

            self._battery_level -= energy

            self._water_capacity -= water


class AlertLevel(Enum):
    low = "low"
    middle = "middle"
    high = "high"


class SecurityRobot(Robot):
    def __init__(
        self,
        dangerous_items: list[str],
        min_speed: int,
        alert_level: AlertLevel,
        name: str | None = None,
        battery_level: int = 100,
        status: RoboStatus = RoboStatus.off,
    ):
        super().__init__(name, battery_level, status)
        self._alert_level = alert_level
        self._min_speed = min_speed
        self._dangerous_items = dangerous_items

    def show_info(self):
        super().show_info()
        print(f"Alert Level: {self._alert_level}")
        print(f"Mining Speed: {self._min_speed}")
        print(f"Dangerous Items: {self._dangerous_items}")

    def turn_off(self):
        self._status = RoboStatus.off
        self._alert_level = AlertLevel.low

    def add_dangerous_item(self, dangerous_item: str):
        if dangerous_item not in self._dangerous_items:
            self._dangerous_items.append(dangerous_item)

    def remove_dangerous_item(self, dangerous_item: str):
        if dangerous_item in self._dangerous_items:
            self._dangerous_items.remove(dangerous_item)

    def detect(self, speed: int, item: str):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        if speed < self._min_speed:
            print("Not enough speed")
            return

        if speed > self._min_speed * 1.5:
            if self._alert_level != AlertLevel.high:
                self._alert_level = AlertLevel.middle
            print(f"Speed is high,alert level is {self._alert_level}")
            return

        if item in self._dangerous_items:
            self._alert_level = AlertLevel.high
            print(f"Danger detected, alert level is {self._alert_level}")
            return


class AssistanceRobot(Robot):
    def __init__(
        self,
        tasks: list[str] | None = None,
        current_task: str | None = None,
        name: str = None,
        battery_level: int = 100,
        status: RoboStatus = RoboStatus.off,
    ):
        super().__init__(name, battery_level, status)

        if tasks is None:
            tasks = []

        if current_task is None:
            current_task = None

        self._tasks = tasks
        self._current_task = current_task

    def show_info(self):
        super().show_info()
        print(f"Robot tasks: {self._tasks}")
        print(f"Current Task: {self._current_task}")

    def add_task(self, task: str):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        if task not in self._tasks:
            self._tasks.append(task)

    def change_current_task(self):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        if self._tasks == []:
            print("No tasks")
            return

        if not self._current_task:
            print("No current task")
            return

        print(f"Tasks: {self._tasks}")

        task = str(input("Enter new current task: "))

        if task not in self._tasks:
            print("Task not found")
            return

        self._current_task = task

    def execute_task(self):
        if self._status == RoboStatus.off:
            print("Robot is off")
            return

        if self._tasks == []:
            print("No tasks")
            return

        if not self._current_task:
            print("No current task")
            return

        print(f"Task: {self._current_task} is done")

        self._tasks.remove(self._current_task)
        self._current_task = self._tasks[0]
