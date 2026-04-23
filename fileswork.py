import json


def load_data(filename: str = "password.json") -> dict[str, str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        # Якщо файлу немає або він порожній, повертаємо порожній словник
        return {}


def save_data(data: dict[str, str], filename: str = "password.json") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_user(data: dict[str, str]) -> None:
    input_login = input("Введіть логін: ")

    if input_login in data:
        print("Користувач існує!")
        return

    password = input("Введіть пароль: ")
    data[input_login] = password

    # Зберігаємо оновлені дані у файл
    save_data(data)
    print(f"Користувача {login} успішно додано.")


def delete_user(data: dict[str, str]) -> None:
    input_login = input("Введіть логін: ")

    if input_login not in data:
        print("Користувач відсутній!")
        return

    del data[input_login]

    # Важливо: викликаємо збереження, щоб оновити JSON-файл
    save_data(data)
    print("Користувача видалено")

def change_password(data: dict[str, str]) -> None:
    input_login = str(input("Enter your login"))

    if input_login not in data:
        print("User not found!")
        return

    new_password = str(input("Enter your new password"))
    data[input_login] = new_password
    save_data(data)

def login(data: dict[str, str]) -> None:
    input_login= input("Enter your login: ")

    if input_login not in data:
        print("User not found!")
        return

    input_password = input("Enter your password: ")

    if input_password != data[input_login]:
        print("Incorrect password!")
        return

    print("You are now logged in!")

# Приклад використання:
# current_data = load_data()
# add_user(current_data)