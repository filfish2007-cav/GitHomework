# Короче, нам нужно навести порядок в бэкенде игровых автоматов. Сейчас там каша, расширять систему невозможно. Переводим всё на рельсы нормального ООП.
#
# Вот тебе задача на спринт.
#
# ### Что нужно сделать:
#
# 1. **Сделай абстрактный базовый класс `Machine`.** * Напрямую его создавать должно быть нельзя.
# * Зашей туда обязательный абстрактный метод для расчета стоимости сессии `calculate_cost(hours)`. Без него дочерние классы собираться не должны.
# * Конструктор должен принимать `id` и `hourly_rate`. Сделай базовую валидацию: ставка только положительная, а ID должен быть строго определенного формата (например, `MAC-1234`).
# * Для валидации ID оформи внутри **статический метод**, чтобы не плодить внешние функции.
# * Там же в базовом классе нужен **метод класса (`@classmethod`)**, который будет работать как альтернативный конструктор — чтобы мы могли развернуть объект из обычной строки конфига типа `"MAC-1024,15.5"`.
#
#
# 2. **Реализуй три конкретных автомата (наследника):**
# * Обычный `ArcadeMachine`.
# * `VRBooth` (со шлемом, там логика расчета стоимости зависит от того, нужен ли клиенту инструктор).
# * `RacingSimulator` (динамический стенд, там к стоимости идет наценка, если включена гидравлика).
# * *Каждый из них должен по-своему переопределять абстрактный расчет стоимости.*
#
#
# 3. **Класс-контроллер `ArcadeHall`:**
# * Сюда мы будем загружать наши автоматы в один список.
# * Нужен метод проведения сессии: находим автомат по ID, проверяем, не сломан ли (если сломан — кидаем ошибку), считаем прайс и плюсуем в общую выручку зала.
#
#
#
# Тесты напиши сам, проверь обязательно:
#
# * Чтобы базовый класс не создавался.
# * Чтобы создание через `@classmethod` работало и для наследников (возвращало именно их объект).
# * Чтобы валидация ID отрабатывала до инициализации.
#
# Жду пулл-реквест. Без костылей, пиши чисто.

from abc import ABC, abstractmethod


class Machine(ABC):
    def __init__(self, machine_id: str, hourly_rate: float):
        if not self.validate_id(machine_id):
            raise ValueError(f"Invalid id: {id}")

        self.id = machine_id
        self.hourly_rate = hourly_rate
        self.is_broken = False

    @staticmethod
    def validate_id(id: str) -> bool | None:
        if not id.startswith("MAC-"):
            return False

        if not id[4:].isdigit():
            return False

        return True

    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate

    # 2. СЕТТЕР: Срабатывает, когда мы пишем `machine.hourly_rate = 25.0`
    @hourly_rate.setter
    def hourly_rate(self, value: float):
        if value <= 0:
            raise ValueError("hourly_rate must be positive")
        # Сохраняем реальное значение в "скрытый" атрибут с нижним подчеркиванием
        self._hourly_rate = value

    @classmethod
    def convert_str(cls, data_string: str):
        machine_id, rate_str = data_string.split(",")

        hourly_rate = float(rate_str)

        return cls(machine_id, hourly_rate)

    @abstractmethod
    def calculate_cost(self, hours: float) -> float:
        pass


class ArcadeMachine(Machine):
    def calculate_cost(self, hours: float) -> float:
        return hours * self.hourly_rate


class VRBooth(Machine):
    def __init__(self, machine_id: str, hourly_rate: float, instructor: bool = False):
        super().__init__(machine_id, hourly_rate)
        self.instructor = instructor

    def calculate_cost(self, hours: float) -> float:
        if self.instructor:
            return hours * self.hourly_rate + 500
        return hours * self.hourly_rate


class RacingSimulator(Machine):
    def __init__(self, machine_id: str, hourly_rate: float, hybrid: bool = False):
        super().__init__(machine_id, hourly_rate)
        self.hybrid = hybrid

    def calculate_cost(self, hours: float) -> float:
        if self.hybrid:
            return hours * self.hourly_rate + 700
        return hours * self.hourly_rate


class ArcadeHall:
    def __init__(self):
        self.revenue: float = 0
        self.machines: list[Machine] = []

    def __call__(self, machine_id: str, hours: float) -> float:
        target = None
        for machine in self.machines:
            if machine.id == machine_id:
                target = machine
                break

        if target is None:
            raise ValueError(f"No machine has been found by id: {machine_id}")

        if target.is_broken:
            raise RuntimeError(f"Machine {machine_id} is broken")

        session_cost = target.calculate_cost(hours)

        self.revenue += session_cost

        print(
            f"Session machine {machine_id} cost: {session_cost}, Total earned: {self.revenue}"
        )

        return session_cost

    def add_machine(self, machine: Machine):
        for existing_machine in self.machines:
            if existing_machine.id == machine.id:
                raise ValueError(f"Machine {machine.id} already exists")

        self.machines.append(machine)


# Создаем зал
hall = ArcadeHall()

# Создаем разные автоматы (используя правильные конструкторы)
arcade = ArcadeMachine("MAC-1111", 10.0)
vr_zone = VRBooth("MAC-2222", 50.0, instructor=True)  # с инструктором

# Добавляем их в зал
hall.add_machine(arcade)
hall.add_machine(vr_zone)

# Проводим сессии
hall("MAC-1111", 2)  # Спишет 20.0 (2 * 10)
hall("MAC-2222", 2)  # Спишет 600.0 (2 * 50 + 500)

# Проверяем выручку
print(f"Итоговая касса зала: {hall.revenue}")  # Выведет 620.0

# Проверяем поломку
arcade.is_broken = True
# hall.use_machine("MAC-1111", 1) # Тут код упадет с aошибкой RuntimeError (автомат сломан)
