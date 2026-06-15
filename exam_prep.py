# -----------------------------------------------------------------
# -----------------------TASK MANAGER----------------------------
# -----------------------------------------------------------------


class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.status = "нове"

    def __str__(self):
        return (
            f"Назва: {self.title} | Статус: [{self.status}]\nОпис: {self.description}\n"
        )


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str, description: str):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"Завдання '{title}' успішно додано.")

    def remove_task(self, title: str):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.")
                return
        print(f"Завдання з назвою '{title}' не знайдено.")

    def complete_task(self, title: str):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.status = "виконано"
                print(f"Завдання '{title}' позначено як виконане.")
                return
        print(f"Завдання з назвою '{title}' не знайдено.")

    def show_all(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return
        print("\n--- Список всіх завдань ---")
        for task in self.tasks:
            print(task)


def main_task_manager():
    manager = TaskManager()
    while True:
        print("\n--- МЕНЕДЖЕР ЗАВДАНЬ ---")
        print("1 — Додати завдання")
        print("2 — Видалити завдання")
        print("3 — Позначити як виконане")
        print("4 — Показати всі завдання")
        print("0 — Вийти")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            title = input("Введіть назву завдання: ").strip()
            description = input("Введіть опис завдання: ").strip()
            if title:
                manager.add_task(title, description)
            else:
                print("Назва не може бути порожньою.")
        elif choice == "2":
            title = input("Введіть назву завдання для видалення: ").strip()
            manager.remove_task(title)
        elif choice == "3":
            title = input("Введіть назву виконаного завдання: ").strip()
            manager.complete_task(title)
        elif choice == "4":
            manager.show_all()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Некоректне введення. Спробуйте ще раз.")


# if __name__ == "__main__":
#     main_task_manager()

# -----------------------------------------------------------------
# -----------------------LIBRARY SYSTEM----------------------------
# -----------------------------------------------------------------


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Доступна" if self.is_available else "Видана"
        return f"'{self.title}' — {self.author} [{status}]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Книгу '{title}' додано до бібліотеки.")

    def issue_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"Книгу '{book.title}' успішно видано.")
                else:
                    print(f"Книга '{book.title}' вже видана іншому читачеві.")
                return
        print(f"Книги з назвою '{title}' немає в бібліотеці.")

    def return_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Книгу '{book.title}' успішно повернено.")
                else:
                    print(f"Книга '{book.title}' вже знаходиться в бібліотеці.")
                return
        print(f"Книги з назвою '{title}' немає в базі даних бібліотеки.")

    def show_all(self):
        if not self.books:
            print("У бібліотеці немає книг.")
            return
        print("\n--- Каталог книг ---")
        for book in self.books:
            print(book)

    def search_book(self, title: str):
        found_books = [
            book for book in self.books if title.lower() in book.title.lower()
        ]
        if not found_books:
            print(f"За запитом '{title}' нічого не знайдено.")
            return
        print("\n--- Результати пошуку ---")
        for book in found_books:
            print(book)


def main_library():
    library = Library()
    # Дефолтні книги для зручності тестування
    library.add_book("Кобзар", "Тарас Шевченко")
    library.add_book("Тигролови", "Іван Багряний")

    while True:
        print("\n--- БІБЛІОТЕЧНА СИСТЕМА ---")
        print("1 — Додати книгу")
        print("2 — Видати книгу")
        print("3 — Повернути книгу")
        print("4 — Показати всі книги")
        print("5 — Пошук книги")
        print("0 — Вийти")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            title = input("Введіть назву книги: ").strip()
            author = input("Введіть автора книги: ").strip()
            if title and author:
                library.add_book(title, author)
            else:
                print("Назва та автор не можуть бути порожніми.")
        elif choice == "2":
            title = input("Введіть назву книги для видачі: ").strip()
            library.issue_book(title)
        elif choice == "3":
            title = input("Введіть назву книги для повернення: ").strip()
            library.return_book(title)
        elif choice == "4":
            library.show_all()
        elif choice == "5":
            title = input("Введіть назву (або її частину) для пошуку: ").strip()
            library.search_book(title)
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Некоректне введення. Спробуйте ще раз.")


# if __name__ == "__main__":
#     main_library()

# -----------------------------------------------------------------
# -----------------------ATM SIMULATOR-----------------------------
# -----------------------------------------------------------------


class Account:
    def __init__(self, owner: str, pin: str, initial_balance: float):
        self.owner = owner
        self.pin = pin
        self.balance = initial_balance


class ATM:
    def __init__(self):
        # Використовуємо словник, де ключ — ім'я власника (у нижньому регістрі для зручності пошуку)
        self.accounts = {}

    def create_account(self, owner: str, pin: str, initial_balance: float):
        key = owner.lower()
        if key in self.accounts:
            print(f"Рахунок на ім'я {owner} вже існує.")
            return
        if initial_balance < 0:
            print("Початковий баланс не може бути від'ємним.")
            return

        self.accounts[key] = Account(owner, pin, initial_balance)
        print(f"Рахунок для {owner} успішно створено.")

    def find_account(self, owner: str) -> Account:
        return self.accounts.get(owner.lower(), None)


def main_atm():
    atm = ATM()

    while True:
        print("\n--- СИМУЛЯТОР БАНКОМАТУ ---")
        print("1 — Створити рахунок")
        print("2 — Поповнити рахунок")
        print("3 — Зняти гроші")
        print("4 — Показати баланс")
        print("0 — Вийти")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            owner = input("Введіть ім'я власника: ").strip()
            pin = input("Введіть PIN (4 цифри): ").strip()
            try:
                balance = float(input("Введіть початковий баланс: "))
                if owner and pin:
                    atm.create_account(owner, pin, balance)
                else:
                    print("Ім'я та PIN не можуть бути порожніми.")
            except ValueError:
                print("Помилка: баланс має бути числом.")

        elif choice == "2":
            owner = input("Введіть ім'я власника: ").strip()
            account = atm.find_account(owner)
            if account:
                pin = input("Введіть PIN: ").strip()
                if account.pin == pin:
                    try:
                        amount = float(input("Введіть суму для поповнення: "))
                        if amount > 0:
                            account.balance += amount
                            print(
                                f"Рахунок поповнено. Новий баланс: {account.balance:.2f} грн."
                            )
                        else:
                            print("Сума поповнення має бути більшою за 0.")
                    except ValueError:
                        print("Помилка: сума має бути числом.")
                else:
                    print("Неправильний PIN-код.")
            else:
                print("Рахунок не знайдено.")

        elif choice == "3":
            owner = input("Введіть ім'я власника: ").strip()
            account = atm.find_account(owner)
            if account:
                pin = input("Введіть PIN: ").strip()
                if account.pin == pin:
                    try:
                        amount = float(input("Введіть суму для зняття: "))
                        if amount <= 0:
                            print("Сума зняття має бути більшою за 0.")
                        elif amount > account.balance:
                            print("Недостатньо коштів на рахунку.")
                        else:
                            account.balance -= amount
                            print(
                                f"Операція успішна. Знято: {amount:.2f} грн. Залишок: {account.balance:.2f} грн."
                            )
                    except ValueError:
                        print("Помилка: сума має бути числом.")
                else:
                    print("Неправильний PIN-код.")
            else:
                print("Рахунок не знайдено.")

        elif choice == "4":
            owner = input("Введіть ім'я власника: ").strip()
            account = atm.find_account(owner)
            if account:
                pin = input("Введіть PIN: ").strip()
                if account.pin == pin:
                    print(
                        f"Поточний баланс рахунку {account.owner}: {account.balance:.2f} грн."
                    )
                else:
                    print("Неправильний PIN-код.")
            else:
                print("Рахунок не знайдено.")

        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Некоректне введення. Спробуйте ще раз.")


# if __name__ == "__main__":
#     main_atm()

## тільки зараз дізнався що атрибути об'єкта класу зберігаються у прихований словник це цікаво
