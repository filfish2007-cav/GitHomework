import json
import pickle
#
# def add_product(items: list[str]) -> None:
#     product = str(input("Product name to add: "))
#     items.append(product)
#     print(f"{product} added.")
#
# def show_info(items: list[str]) -> None:
#     print(f"here are your items: ")
#     for item in items:
#         print(f"{item}")
#
#
# def save_info_json(items: list[str],filename: str = "products.json") -> None:
#     with open(filename, "w") as file:
#         json.dump(items, file, indent=4)
#         print(f"{filename} saved.")
#
# def save_info_pickle(items: list[str], filename: str = "products.pickle") -> None:
#     with open(filename, "wb") as file:
#         pickle.dump(items, file)
#         print(f"{filename} saved.")
#
# def load_info_pickle(items: list[str], filename: str = "products.pickle") -> list[str]:
#     with open(filename, "rb") as file:
#         return pickle.load(file)
#
# def load_info_json(filename: str = "products.json") -> list[str]:
#     with open(filename, "r") as file:
#         return json.load(file)
#
# products = []

### task 2

# import json
# import pickle
#
# class Student:
#     def __init__(self, name: str, specialization: str, grades: list[int]):
#         self.name = name
#         self.specialization = specialization
#         self.grades = grades
#
#     def to_dict(self):
#         """Converts instance to a dictionary."""
#         return {
#             "name": self.name,
#             "specialization": self.specialization,
#             "grades": self.grades
#         }
#
#     def show_info(self):
#         print(f" Name: {self.name}")
#         print(f" Specialization: {self.specialization}")
#         print(f" Grades: {self.grades}")
#
# st1 = Student("abdul", "engineer", [2, 12, 5, 7])
# st2 = Student("kiril", "philosophy", [3, 9, 5, 7])
# st3 = Student("goi", "religion", [4, 3, 8, 9])
#
# studs = [st1, st2, st3]
#
# def get_studs_as_dicts():
#     return [s.to_dict() for s in studs]
#
# def save_studs_json():
#     with open("studs.json", "w") as file:
#         json.dump(get_studs_as_dicts(), file, indent=4)
#
# def save_studs_pickle():
#     with open("studs.pickle", "wb") as file:
#         pickle.dump(get_studs_as_dicts(), file)
#
# def load_studs_json():
#     try:
#         with open("studs.json", "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
#
# def load_studs_pickle():
#     try:
#         with open("studs.pickle", "rb") as file:
#             return pickle.load(file)
#     except FileNotFoundError:
#         return []

# # Завдання 3
# # Є словник з друзями, де ключ - людина, а значення -
# # список друзів. Користувач вводить імена двох людей,
# #які є друзями, повторює це певну кількість разів,
# #після чого дані зберігаються у файл.
# #Завантажте дані назад та виведіть на екран.

import json
import pickle

friends = {
    "John Pork": ["Max", "Alex", "LeBron"],
    "Jimmy Butler": ["Joakim", "Nate", "Wade"],
    "J.J Reddick": ["PJ", "Jrue", "Scoot"]
}

def add_friend(person: str, new_friend: str) -> None:
    if person in friends:
        friends[person].append(new_friend)
        print(f"Added {new_friend} to {person}'s list.")
    else:
        print(f"Error: {person} not found in records.")

def save_friends_json() -> None:
    with open("friends.json", "w") as file:
        json.dump(friends, file, indent=4)

def save_friends_pickle() -> None:
    with open("friends.pickle", "wb") as file:
        pickle.dump(friends, file)

def load_friends_pickle():
    try:
        with open("friends.pickle", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def load_friends_json():
    try:
        with open("friends.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

ch1 = input("Enter person name: ")
ch2 = input("Enter friend to add: ")

add_friend(ch1, ch2)

save_friends_json()
print("Updated Data:", load_friends_json())



