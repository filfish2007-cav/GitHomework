# # task 1

# from math import pi
#
#
# class Rectangle:
#     def __init__(self, side: float):
#         self.side = side
#
#     def perimeter(self) -> float:
#         return self.side * 4
#
#     def show_info(self):
#         print(f"Прямоугольник со стороной {self.side}. Периметр: {self.perimeter()}")
#
#
# class Circle:
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def perimeter(self) -> float:
#         return round(self.radius * 2 * pi)
#
#     def show_info(self):
#         print(f"Периметр круга: {self.perimeter():.2f}")
#
#
# class Triangle:
#     def __init__(self, side1: float, side2: float, side3: float):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def perimeter(self) -> float:
#         return self.side1 + self.side2 + self.side3
#
#     def show_info(self):
#         print(f"Периметр треугольника: {self.perimeter()}")
#
#
#
# def create_figure() -> Triangle | Rectangle | Circle:
#     figure = str(input("which figure u want to create?: ")).strip().lower()
#
#     if figure == "rectangle":
#
#         side = float(input("enter the side of the rectangle: "))
#         return Rectangle(side)
#
#     elif figure == "circle":
#         radius = float(input("enter the radius of the circle: "))
#         return Circle(radius)
#
#     elif figure == "triangle":
#         side1 = float(input("enter the first side of the triangle: "))
#         side2 = float(input("enter the second side of the triangle: "))
#         side3 = float(input("enter the third side of the triangle: "))
#         return Triangle(side1, side2, side3)
#     else:
#         raise ValueError("the figure you entered is not valid")
#
# try:
#     figures = []
#     for i in range(3):
#         figura = create_figure()
#         figura.show_info()
#         p = figura.perimeter()
#         figures.append(p)
#     print(figures)
# except ValueError:
#     print("This figure is not available")

# # task 2

# class Manager:
#     def __init__(self, name: str, base_salary: int):
#         self.name = name
#         self.base_salary = base_salary
#
#     def get_salary(self):
#         return self.base_salary
#
#     def show_info(self):
#         print(f"Менеджер: {self.name}, Зарплата: {self.get_salary()}")
#
#
# class Developer:
#     def __init__(self, name: str, base_salary: int, work_experience: int):
#         self.name = name
#         self.base_salary = base_salary
#         self.work_experience = work_experience
#
#     def get_salary(self):
#         if self.work_experience > 4:
#             return self.base_salary * 1.2
#         return self.base_salary
#
#     def show_info(self):
#         print(f"Розробник: {self.name}, Досвід: {self.work_experience}р., Зарплата: {self.get_salary()}")
#
#
# class Intern:
#     def __init__(self, name: str, base_salary: int):
#         self.name = name
#         self.base_salary = base_salary
#
#     def get_salary(self):
#         return self.base_salary * 0.5
#
#     def show_info(self):
#         print(f"Стажер: {self.name}, Зарплата: {self.get_salary()}")
#
#
# def create_worker() -> Manager | Developer | Intern:
#     employee_type = input("Тип співробітника (manager/developer/intern): ").strip().lower()
#
#     name = input("Ім'я: ").strip()
#     base_salary = int(input("Базова ставка: "))
#
#     if employee_type == "manager":
#         return Manager(name, base_salary)
#
#     elif employee_type == "developer":
#         experience = int(input("Досвід (років): "))
#         return Developer(name, base_salary, experience)
#
#     elif employee_type == "intern":
#         return Intern(name, base_salary)
#     else:
#         raise ValueError("Такого співробітника нема")
#
# workers = []
#
# try:
#     for i in range(3):
#         print(f"\nВвід даних для співробітника №{i+1}:")
#         new_worker = create_worker()
#         workers.append(new_worker)
#
#     print("\n--- Звіт по зарплатам ---")
#     for worker in workers:
#         worker.show_info()
#
# except ValueError as e:
#     print(f"Помилка: {e}")

