# # task 1

import json
from typing import Any
#
#
# def load_data(filename: str = "password.json") -> dict[str, str]:
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             data = json.load(file)
#         return data
#     except (FileNotFoundError, json.JSONDecodeError):
#         # Якщо файлу немає або він порожній, повертаємо порожній словник
#         return {}
#
#
# def save_data(data: dict[str, str], filename: str = "password.json") -> None:
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#
#
# def add_user(data: dict[str, str]) -> None:
#     input_login = input("Введіть логін: ")
#
#     if input_login in data:
#         print("Користувач існує!")
#         return
#
#     password = input("Введіть пароль: ")
#     data[input_login] = password
#
#     # Зберігаємо оновлені дані у файл
#     save_data(data)
#     print(f"Користувача {login} успішно додано.")
#
#
# def delete_user(data: dict[str, str]) -> None:
#     input_login = input("Введіть логін: ")
#
#     if input_login not in data:
#         print("Користувач відсутній!")
#         return
#
#     del data[input_login]
#
#     # Важливо: викликаємо збереження, щоб оновити JSON-файл
#     save_data(data)
#     print("Користувача видалено")
#
# def change_password(data: dict[str, str]) -> None:
#     input_login = str(input("Enter your login"))
#
#     if input_login not in data:
#         print("User not found!")
#         return
#
#     new_password = str(input("Enter your new password"))
#     data[input_login] = new_password
#     save_data(data)
#
# def login(data: dict[str, str]) -> None:
#     input_login= input("Enter your login: ")
#
#     if input_login not in data:
#         print("User not found!")
#         return
#
#     input_password = input("Enter your password: ")
#
#     if input_password != data[input_login]:
#         print("Incorrect password!")
#         return
#
#     print("You are now logged in!")
#
#
# def main_menu():
#     # 1. Завантажуємо дані при старті програми
#     users_data = load_data()
#
#     while True:
#         print("\n--- ГОЛОВНЕ МЕНЮ ---")
#         print("1. Зареєструватися (add_user)")
#         print("2. Увійти (login_user)")
#         print("3. Змінити пароль (change_password)")
#         print("4. Видалити акаунт (delete_user)")
#         print("5. Вийти з програми")
#
#         choice = input("\nОберіть дію (1-5): ")
#
#         if choice == "1":
#             add_user(users_data)
#         elif choice == "2":
#             login(users_data)
#         elif choice == "3":
#             change_password(users_data)
#         elif choice == "4":
#             delete_user(users_data)
#         elif choice == "5":
#             print("Програма завершена. До побачення!")
#             break
#         else:
#             print("Неправильний вибір, спробуйте ще раз.")
#
#
# # Запуск програми
# if __name__ == "__main__":
#     main_menu()

class Cart:
    def __init__(self,user: str) -> None:
        self._user = user
        self._items = []
        self._total = 0

    def add_item(self,item: str,price: int) -> None:
        self._items.append(item)
        self._total += price

    def delete_item(self,item: str,price: int) -> None:
        if item not in self._items:
            print("Item not found!")
            return

        self._items.remove(item)
        self._total -= price

    def show_info(self) -> None:
        print(f"user: {self._user}, total: {self._total}")
        print(f"items: {self._items}")

    def save(self, filename: str = "cart.json") -> None:
        data = {"user": self._user,
                "items": self._items,
                "total": self._total}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self, filename: str = "cart.json") -> None:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        self._user = data["user"]
        self._items = data["items"]
        self._total = data["total"]

# john = Cart("John")
#
# john.add_item("Banana", 100)
# john.add_item("Apple", 200)
# john.load()
# john.show_info()

# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і
# створюються відповідні змінні size, background
# color, …

with open("settings.json", "w", encoding="utf-8") as file:
    data = {
            "size" : "500x600",
            "color" : "grey",
            "button_color" : "bright grey",
            "placement_buttons" : [100,50],
            "instcructions" : " Be a simple kind of man"}

    json.dump(data,file, indent=4, ensure_ascii=False)

def load_settings() -> dict[str, Any]:
    with open("settings.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def save_settings(data: dict) -> None:
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def change_size(new_size: str) -> None:
    data = load_settings()
    data["size"] = new_size
    save_settings(data)

def change_color(new_color: str) -> None:
    data = load_settings()
    data["color"] = new_color
    save_settings(data)

def show_info() -> None:
    data = load_settings()
    new = json.dumps(data, indent=4, ensure_ascii=False)
    print(new)

change_size("4000x60")
change_color("blue")
show_info()




