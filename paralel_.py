import threading
import json
# # task 1

# def find_max(nums):
#     result["max"] = max(nums)
#
# def find_min(nums):
#     result["min"] = min(nums)
#
# nums = list(map(int,input("Enter numbers: ").split(", ")))
#
# result = {}
#
# thread_max = threading.Thread(target=find_max, args=(nums, result))
# thread_min = threading.Thread(target=find_min, args=(nums, result))
#
# thread_max.start()
# thread_min.start()
#
# thread_max.join()
# thread_min.join()
#
# print(result)

# # task 2

# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік зна-
# ходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

# def find_sum(nums, result):
#     result["sum"] = sum(nums)
#
# def find_avg(nums, result):
#     result["avg"] = sum(nums) / len(nums)
#
# nums = list(map(int,input("Enter numbers: ").split(", ")))
#
# result = {}
#
# thread_sum = threading.Thread(target=find_sum, args=(nums,result))
#
# thread_avg = threading.Thread(target=find_avg, args=(nums,result))
#
# thread_sum.start()
# thread_avg.start()
#
# thread_sum.join()
# thread_avg.join()
#
# print(result)

# # task 3


# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

# def parne(listik: list[int]):
#     with open("parne.txt", "w") as f:
#         for x in listik:
#             if x % 2 == 0:
#                 f.write(str(x) + "\n")
#
# def neparne(listik: list[int]):
#     with open("neparne.txt", "w") as f:
#         for x in listik:
#             if x % 2 != 0:
#                 f.write(str(x) + "\n")
#
# file_path = input("Enter file path: ")
#
# with open(file_path, "r") as f:
#     nums = f.readline().split()
#     nums = list(map(int, nums))
#
# thread_parne = threading.Thread(target=parne, args=(nums,))
# thread_neparne = threading.Thread(target=neparne, args=(nums,))
# thread_parne.start()
# thread_neparne.start()
#
# thread_parne.join()
# thread_neparne.join()

# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

# # task 4

from threading import Thread

def search(path, word):
    with open(path, 'r', encoding='utf-8') as f:
        found = word in f.read()
    print(f"Знайдено: {found}")

file_path = input("Шлях: ")
word_to_find = input("Слово: ")

t = Thread(target=search, args=(file_path, word_to_find))
t.start()
t.join()



