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


