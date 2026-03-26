# # task 1
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

class Student:

    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("John", 25)
student2 = Student("Michael", 35)
student3 = Student("Bob", 35)

students = [student1, student2, student3]

for stu in students:
    print(f"Student {students.index(stu)+1}:")
    print()
    stu.display()
    print()