# -----------------------------------------------------------------
# ----------------FUNCTIONS LOOPS BASICS(PART 1)-------------------
# -----------------------------------------------------------------
import random
from datetime import datetime

# task 1 (including values)

# a = int(input("input first value: "))
# b = int(input("input second value: "))
#
# summa = 0
# for i in range(a, b+1):
#     summa += i
#
# print(summa)

# # task 2

# summa = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         summa += i
#
# print(summa)

# # # task 3 (separate row for each letter)

# string = str(input())
#
# for i in string:
#     print(i)

# # # # task 4

# import random
# option one
# listochok = list(random.sample(range(0,101), 10))
# option two
# listochok_2 = list(random.randint(0,1000) for _ in range(19))

# res = [num for num in listochok_2 if num % 2 == 0]

# print(res)

# # # # # task 5

# def converter(sps: list[str]) -> list[str]:
#     result = [string for string in sps if string[0] == string[0].upper()]
#     return result
#
# print(converter(["Obeziana","obeziana","Bobab","bobap"]))

# # # # # # task 6

# def converter_2(sps: list[str]) -> list[str]:
#     result = [string for string in sps if "Python" in string]
#     return result
#
# print(converter_2(["Python programming language", "nopython"]))

# # # # # # # task 7

# dictionary = dict()
#
# def add(key, value):
#     if key not in dictionary:
#         dictionary[key] = value
#     else:
#         print("such value already exists")
#
#     print(f"key {key} and value {value} were added to dictionary")
#
# def remove(key):
#     if key in dictionary:
#         del dictionary[key]
#     else:
#         print("such key does not exist")
#
#     print(f"key {key} and value {dictionary[key]} were deleted from dictionary")
#
# def get(key):
#     if key in dictionary:
#         print(f"key: {key}, value:{dictionary[key]}")
#     else:
#         return "such key does not exist"
#
# add("chicago","bulls")
# get("chicago")

# # # # # # # # task 8

# data = [(1, 8), (3, 4), (2, 10)]
#
# def sorter(sps : list[tuple[int,int]]) -> list[tuple[int,int]]:
#     result = sorted(sps, key = lambda x: x[1])
#     return result
#
# print(sorter(data))

# -----------------------------------------------------------------
# ---------------OBJECT ORIENTED PROGRAMMING (PART 2)--------------
# -----------------------------------------------------------------


class WebPage:
    """
    Клас, що представляє окрему веб-сторінку.

    Атрибути:
        headline (str): Заголовок сторінки.
        content (str): Текстовий вміст (контент) сторінки.
        release_date (datetime): Дата та час публікації.
        key (int): Унікальний цифровий ідентифікатор сторінки.
    """

    def __init__(
        self, headline: str, content: str, release_date: datetime, key: None | int
    ):
        self.headline = headline
        self.content = content
        self.release_date = release_date
        self.key = key if key is not None else random.randint(100000, 999999)

    def __str__(self):
        """Повертає текстове представлення сторінки для виведення на екран."""
        return f"{self.headline}: \n {self.content} | \n \n {self.release_date}"


class Website:
    """
    Клас, що представляє вебсайт, який містить набір сторінок.

    Атрибути:
        name (str): Назва сайту.
        url (str): Посилання (URL) сайту.
        pages_list (list[WebPage]): Список об'єктів сторінок, які належать сайту.
    """

    def __init__(self, name: str, url: str, pages_list=None):
        self.name = name
        self.url = url
        if pages_list is None:
            self.pages_list = []
        else:
            self.pages_list = pages_list

    def __str__(self):
        """Повертає загальну інформацію про сайт та список його сторінок у вигляді рядка."""
        return f"{self.name}: \n {self.url} | \n \n {self.pages_list}"

    def add_page(self, headline: str, content: str, release_date=datetime.now()):
        """
        Створює та додає нову сторінку на сайт, якщо сторінки з таким заголовком ще немає.

        Аргументи:
            headline (str): Заголовок нової сторінки.
            content (str): Контент нової сторінки.
            release_date (datetime): Дата публікації (за замовчуванням поточний час).

        Повертає:
            str: Повідомлення про успішне додавання з ID сторінки або повідомлення про помилку.
        """
        key = random.randint(100000, 999999)
        page = WebPage(headline, content, release_date, key=key)
        for i in self.pages_list:
            if i.headline == headline:
                return "page already exist"
        self.pages_list.append(page)
        return f"page added id: {key}"

    def del_page(self, key: int):
        """
        Видаляє сторінку з сайту за її унікальним ID.

        Аргументи:
            key (int): Ідентифікатор сторінки, яку потрібно видалити.

        Повертає:
            str: Повідомлення про успішне видалення або про те, що сторінка не існує.
        """
        page = None
        for i in self.pages_list:
            if i.key == key:
                page = i
                break
        else:
            return "page does not exist"
        self.pages_list.remove(page)
        return f"page deleted id: {key} "

    def get_page_info(self, key: int):
        """
        Шукає сторінку за ID та повертає інформацію про неї.

        Аргументи:
            key (int): Ідентифікатор шуканої сторінки.

        Повертає:
            str: Текстове представлення сторінки або повідомлення про помилку.
        """
        for page in self.pages_list:
            if page.key == key:
                return str(page)
        else:
            return "page does not exist"


def main():
    """
    Головна функція програми.
    Запускає консольний інтерфейс (CMS) для створення сайтів та керування їхніми сторінками.
    """
    # Сховище для всіх створених користувачем сайтів
    websites: list[Website] = []

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Створити новий сайт")
        print("2. Показати всі сайти та їх сторінки")
        print("3. Додати сторінку на сайт")
        print("4. Видалити сторінку за ID")
        print("5. Вихід")

        choice = input("Ваш вибір: ").strip()

        # Опція 1: Створення нового веб-сайту
        if choice == "1":
            name = input("Назва сайту: ")
            url = input("URL сайту: ")
            websites.append(Website(name, url))
            print("🎉 Сайт створено!")

        # Опція 2: Виведення списку всіх сайтів та їхнього вмісту
        elif choice == "2":
            if not websites:
                print("Сайтів ще немає.")
            for idx, site in enumerate(websites):
                print(f"{idx}. {site}")

        # Опція 3: Додавання нової сторінки на конкретний сайт
        elif choice == "3":
            if not websites:
                print("Спочатку створить сайт!")
                continue
            site_idx = int(input(f"Оберіть номер сайту (0-{len(websites) - 1}): "))
            headline = input("Заголовок сторінки: ")
            content = input("Контент: ")

            print(websites[site_idx].add_page(headline, content))

        # Опція 4: Видалення сторінки за ID (пошук проходить по всіх сайтах)
        elif choice == "4":
            if not websites:
                print("Сайтів ще немає.")
                continue
            key = int(input("Введіть ID сторінки для видалення: "))

            for site in websites:
                print(site.del_page(key))

        # Опція 5: Вихід з нескінченного циклу та завершення програми
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
