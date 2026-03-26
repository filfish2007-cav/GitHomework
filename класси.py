# # task 1
import math
from operator import index


# class Student:
#
#     def __init__(self, name, age):
#         self.name = name.capitalize()
#         self.age = age
#
#     def display(self):
#         print(self.name)
#         print(self.age)
#
# student1 = Student("John", 25)
# student1.display()

# # task 2

# class Student:
#
#     def __init__(self, name, age):
#         self.name = name.capitalize()
#         self.age = age
#
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#
# student1 = Student("John", 25)
# student2 = Student("Michael", 35)
# student3 = Student("Bob", 35)
#
# students = [student1, student2, student3]
#
# for stu in students:
#     print(f"Student {students.index(stu)+1}:")
#     print()
#     stu.display()
#     print()

# # task 3

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print(f"Radius is {math.pi * self.radius ** 2}")
#
# kolo = Circle(5)
# kolo.area()

# # task 4

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.name = owner.capitalize()
#         self.balance = int(balance)
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Balance: {self.balance}")
#
# user1 = BankAccount("John", 100)
# user1.deposit(50)
# user1.withdraw(20)
# user1.display()

# # task 5
class Car:
    def __init__(self, brand, year, is_ready = False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready
    def start_engine(self):
        self.is_ready = True
        print("The car just started")
    def move(self):
        if self.is_ready:
            print(f"{self.brand} made in {self.year} is Moving ")
        else:
            print(f"{self.brand} made in {self.year} is not Moving ")

car1 = Car("Bentley", 2021)
car1.move()
car1.start_engine()
car1.move()